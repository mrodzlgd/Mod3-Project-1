"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from statsmodels.stats import power as pw

def create_sample_dists(cleaned_data, y_var=None, categories=[]):
    """
    Each hypothesis test will require you to create a sample distribution from your data
    Best make a repeatable function

    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    metro = cleaned_data.loc[cleaned_data['csi'] == 1][y_var]
    non_metro = cleaned_data.loc[cleaned_data['csi'] != 1][y_var]
    
    htest_dfs = [metro,non_metro]

    # Main chunk of code using t-tests or z-tests
    return htest_dfs
    
def get_sample_means(data,sample_size):
    means = []
    for i in range(0,100000):
        a_mean = np.mean(np.random.choice(data, size=sample_size))
        means.append(a_mean)
    return means
    
def Cohen_d(group1, group2):

    # Compute Cohen's d.

    # group1: Series or NumPy array
    # group2: Series or NumPy array

    # returns a floating point number 

    diff = np.mean(group1) - np.mean(group2)

    n1, n2 = len(group1), len(group2)
    var1 = np.var(group1)
    var2 = np.var(group2)

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return d
    

def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


def hypothesis_test_one(cleaned_data,alpha = None):#Total Hospital Charges
    """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the hypothesis test.
    If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data:
    :return:
    """
    # Get data for tests
    comparison_groups = comparison_groups = create_sample_dists(cleaned_data, y_var='average_covered_charges', categories=['metro','non_metro'])

    ###
    
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    
   # metro_means = get_sample_means(comparison_groups[0],100)
   # non_metro_means = get_sample_means(comparison_groups[1],100)
   
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]
    
    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    d = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[0]
    coh_d = Cohen_d(metro_sample, non_metro_sample)
    power = pw.tt_ind_solve_power(effect_size=d, nobs1=100, alpha=alpha, power=None, ratio=1.0, alternative='two-sided')
    ###


    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference in charges between Hospitals in Metro and Non-Metro Areas')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status
    
    
def hypothesis_test_two(cleaned_data,alpha = None):#out_of_pocket
     # Get data for tests
    comparison_groups = comparison_groups = create_sample_dists(cleaned_data, y_var='out_of_pocket', categories=['metro','non_metro'])

    ###
   
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    
    metro_means = get_sample_means(comparison_groups[0],100)
    non_metro_means = get_sample_means(comparison_groups[1],100)
   
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]
    
    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    d = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[0]
    coh_d = Cohen_d(metro_sample, non_metro_sample)
    power = pw.tt_ind_solve_power(effect_size=d, nobs1=100, alpha=alpha, power=None, ratio=1.0, alternative='two-sided')
  
  ###


    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference in out-of-pocket cost for patients using Hospitals in Metro vs. Non-Metro Areas')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status

def hypothesis_test_three(cleaned_data,alpha = None):
     # Get data for tests
    comparison_groups = comparison_groups = create_sample_dists(cleaned_data, y_var='perc_covered', categories=['metro','non_metro'])

    ###
    
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    
    metro_means = get_sample_means(comparison_groups[0],100)
    non_metro_means = get_sample_means(comparison_groups[1],100)
   
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]
    
    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    d = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[0]
    coh_d = Cohen_d(metro_sample, non_metro_sample)
    power = pw.tt_ind_solve_power(effect_size=d, nobs1=100, alpha=alpha, power=None, ratio=1.0, alternative='two-sided')
    ###


    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference in the percentage in the amount of total payments received by Hospitals in Metro vs. Non-Metro Areas for provided services.')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_four():
    pass
