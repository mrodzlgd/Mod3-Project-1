'''Retrieves data from APIs (Google Maps, Census Geocoding API, data.cms.gov)
and joins census data based on latitude and longitude of hospital address'''
import requests
import pandas as pd


def get_hospital_data():
    '''Retrieve hospital data from data.cms.gov API'''
    response = requests.get('https://data.cms.gov/resource/fm2n-hjj6.json')
    resp_json = response.json()
    hosp_data = pd.DataFrame(resp_json)
    hosp_data['full_address'] = hosp_data['provider_street_address'] + ', ' + \
        hosp_data['provider_city'] + ', ' + \
        hosp_data['provider_state']
    return hosp_data


def get_lat_lng(address, api_key):
    '''Retrieve Latitude and Longitude for Address with Google Maps API'''
    format_address = address.replace(' ', '+')
    response = requests.get(
        f'''https://maps.googleapis.com/maps/api/geocode/json?address=
        {format_address}&key={api_key}''')
    if response.status_code != 200:
        return address
    try:
        lat = response.json()[
            'results'][0]['geometry']['viewport']['northeast']['lat']
        lng = response.json()[
            'results'][0]['geometry']['viewport']['northeast']['lng']
        return lat, lng
    except:
        return address


def get_geoid(lat, lng):
    '''Retrieve 2010 Census Data For Latitude and Longitude'''
    vintage = 'Census2010_Census2010'
    benchmark = 'Public_AR_Census2010'
    format_ = 'json'

    fields = {'x': lng,
              'y': lat,
              'vintage': vintage,
              'benchmark': benchmark,
              'format': format_, }

    url = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates'

    response = requests.get(url, params=fields, timeout=5)
    assert response.status_code == 200, 'GEOLOCATOR API ISSUE'
    try:
        geoid = response.json()[
            'result']['geographies']['Census Blocks'][0]['GEOID']
    except:
        geoid = lat, lng
    return geoid


def get_location_data(hosp_data):
    '''Retrieve location info (GEOID) of every unique hospital address'''
    api_key = input('Enter Google Maps API Key: ')
    tract_geoids = []
    unique_addresses = hosp_data.full_address.unique()
    for address in unique_addresses:
        try:
            lat, lng = get_lat_lng(address, api_key)
            geoid = get_geoid(lat, lng)
            tract_geoids.append(geoid)
        except:
            geoid = get_lat_lng(address, api_key)
            tract_geoids.append(geoid)
    location_data = pd.DataFrame(unique_addresses, tract_geoids).reset_index()
    location_data.columns = ['GEOID', 'full_address']
    location_data.GEOID = location_data.GEOID.map(lambda x: x[:-4])
    return location_data


def join_data(hosp_data, location_data):
    '''Join hospital data, location data, and census tract data'''
    census_data = pd.read_excel('./data/censustract-00-10.xlsx', dtype=str)
    location_census_merge = pd.merge(location_data, census_data[[
        'GEOID', 'CSI']], how='left', on='GEOID')
    joined_data = pd.merge(hosp_data, location_census_merge,
                           how='left', on='full_address')
    return joined_data


def get_dirty_data():
    '''Produce dirty_data.csv in ./data/'''
    hosp_data = get_hospital_data()
    location_data = get_location_data(hosp_data[0:5])
    dirty_data = join_data(hosp_data, location_data)
    dirty_data.to_csv('./data/dirty_data')
    return dirty_data
