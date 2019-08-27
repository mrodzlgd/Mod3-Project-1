"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.
Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null
hypothesis" depending on the specified alpha.
"""

import pandas as pd
import numpy as np
import scipy.stats as st
from statsmodels.stats import power as pw
from tqdm import tqdm_notebook


def create_sample_dists(cleaned_data, y_var=None):
    """
    Each hypothesis test will require you to create a sample distribution
    from your data. Best make a repeatable function

    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    metro = cleaned_data.loc[cleaned_data['csi'] == '1'][y_var]
    non_metro = cleaned_data.loc[cleaned_data['csi'] != '1'][y_var]

    htest_dfs = [metro, non_metro]

    return htest_dfs


def get_sample_means(sample, size=100):
    sample_means = []
    for i in range(0, 100000):
        a_mean = np.mean(np.random.choice(sample, size=size))
        sample_means.append(a_mean)

    return sample_means


def cohen_d(group1, group2):

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


def hypothesis_test_one(cleaned_data, alpha=0.5):
    """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the
    hypothesis test.If a value of alpha is entered that is outside of the
    acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data:
    :return:
    """
    comparison_groups = create_sample_dists(cleaned_data,
                                            y_var='average_covered_charges')

    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]

    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    coh_d = abs(cohen_d(metro_sample, non_metro_sample))
    nobs1 = len(non_metro_sample)
    ratio = len(metro_sample)/nobs1
    power = pw.tt_ind_solve_power(effect_size=coh_d, nobs1=nobs1, alpha=alpha,
                                  power=None, ratio=ratio,
                                  alternative='two-sided')

    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"

    print(f'Based on the p value of {p_val} and our aplha of {alpha} \
          we {status.lower()} the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there \
          is a difference in charges between Hospitals in Metro and\
          Non-Metro Areas')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and \
              power of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_two(cleaned_data, alpha=0.5):
    comparison_groups = create_sample_dists(cleaned_data,
                                            y_var='out_of_pocket')
    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]
    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    coh_d = abs(cohen_d(metro_sample, non_metro_sample))
    nobs1 = len(non_metro_sample)
    ratio = len(metro_sample)/nobs1
    power = pw.tt_ind_solve_power(effect_size=coh_d, nobs1=nobs1, alpha=alpha,
                                  power=None, ratio=ratio,
                                  alternative='two-sided')
    ###
    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we \
         {status.lower()} the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that \
          there is a difference in out-of-pocket cost for patients \
          using Hospitals in Metro vs. Non-Metro Areas')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and\
              power of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_three(cleaned_data, alpha=0.5):
    comparison_groups = create_sample_dists(cleaned_data, y_var='perc_covered')
    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]

    p_val = st.ttest_ind(metro_sample, non_metro_sample, equal_var=False)[1]
    coh_d = abs(cohen_d(metro_sample, non_metro_sample))
    nobs1 = len(non_metro_sample)
    ratio = len(metro_sample)/nobs1
    power = pw.tt_ind_solve_power(effect_size=coh_d, nobs1=nobs1, alpha=alpha,
                                  power=None, ratio=ratio,
                                  alternative='two-sided')
    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we\
          {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is \
          a difference in the percentage of charges covered by medicare for \
          Hospitals in Metro vs. Non-Metro Areas for the provided services.')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power \
              of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_four(cleaned_data):
    sig_procs = []
    sig_cohens = []
    for i in tqdm_notebook(cleaned_data.drg_definition.unique()):
        metro = cleaned_data.loc[(cleaned_data.csi == '1') & (
                cleaned_data.drg_definition == i)]['average_covered_charges']
        non_metro = cleaned_data.loc[(cleaned_data.csi != '1') & (
                   cleaned_data.drg_definition == i)][
                   'average_covered_charges']
        if st.ttest_ind(metro, non_metro, equal_var=False)[1] < 0.05:
            sig_procs.append(i)
            sig_cohens.append(cohen_d(metro, non_metro))

    relevant_codes = pd.DataFrame([pd.Series(sig_procs, name='sig_procs'),
                                  pd.Series(sig_cohens, name='cohens_d')]).T

    relevant_codes.sig_procs = relevant_codes.sig_procs.map(
                               lambda x: x[0:3]).astype(int)

    drg = pd.read_csv('data/DRG.csv')
    drg['group_size'] = drg.Code_End-drg.Code_Start

    drg_d = drg.to_dict('records')

    code_ref = []
    for i in range(0, len(drg_d)):
        for c in relevant_codes.sig_procs:
            if drg_d[i]['Code_Start'] <= c <= drg_d[i]['Code_End']:
                code_ref.append({'sig_procs': c, 'Code_Start':
                                 drg_d[i]['Code_Start'],
                                 'Code_End': drg_d[i]['Code_End'],
                                 'Group': drg_d[i]['Description']})
    code_map = pd.DataFrame.from_dict(code_ref)
    code_map['cohens_d'] = relevant_codes.cohens_d

    cum_codes = code_map.groupby('Group').size().reset_index()
    cum_cohen = code_map.groupby('Group').cohens_d.sum().reset_index().cohens_d
    # cum_codes.columns = ['Description', 'num_sig_procs']

    cum_codes['sum_effect'] = cum_cohen
    # cum_codes['avg_effect'] = drg.sum_effect/drg.group_size

    cum_codes.columns = ['Description', 'num_sig_procs', 'sum_effect']

    cum_codes = cum_codes.merge(drg, on='Description')
    cum_codes['avg_effect'] = cum_codes.sum_effect/cum_codes.group_size
    cum_codes['code'] = cum_codes.Description.apply(lambda x: x[0:6])

    return cum_codes
