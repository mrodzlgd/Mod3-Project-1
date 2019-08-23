"""
This module is for your data cleaning.
It should be repeatable.

## PRECLEANING
There should be a separate script recording how you transformed the json api calls into a dataframe and csv.

## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd

def drop_columns(dirty_data):
    dirty_data.drop(columns=['provider_zip_code', 'provider_street_address',
                             'provider_state', 'provider_id', 'provider_city',
                             'hospital_referral_region_hrr_description', 
                             'Unnamed: 0'], inplace=True)
    return dirty_data

def change_data_type(dirty_data):
    dirty_data['average_covered_charges'] = dirty_data['average_covered_charges'].astype(
        float)
    dirty_data['average_medicare_payments'] = dirty_data['average_medicare_payments'].astype(
        float)
    dirty_data['average_total_payments'] = dirty_data['average_total_payments'].astype(
        float)
    dirty_data['total_discharges'] = dirty_data['average_total_payments'].astype(
        int)
    return dirty_data

def add_columns(dirty_data):
    dirty_data['out_of_pocket'] = dirty_data.average_total_payments - \
        dirty_data.average_medicare_payments
    dirty_data['perc_covered'] = dirty_data.average_medicare_payments / \
        dirty_data.average_covered_charges
    return dirty_data

def clean_column_names(dirty_data):
    dirty_data.columns = dirty_data.columns.map(lambda x: x.lower())
    return dirty_data

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    dirty_data = pd.read_csv("./data/dirty_data.csv", dtype=str)

    cleaning_data1 = drop_columns(dirty_data)
    cleaning_data2 = change_data_type(cleaning_data1)
    cleaning_data3 = add_columns(cleaning_data2)
    cleaned_data= clean_column_names(cleaning_data3)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')
    
    return cleaned_data