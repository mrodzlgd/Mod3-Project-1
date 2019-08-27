"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import hypothesis_tests as ht


def plot_distribution(sample_one, label_one, sample_two, label_two, title):
    '''Plot distributions given data and specifications'''
    plt.figure(figsize=(14, 7))
    sns.distplot(sample_one, label=label_one)
    sns.distplot(sample_two, label=label_two)
    plt.legend(loc=0)
    plt.xlabel(title)
    plt.title(title)


def visualization_four(cleaned_data):
    '''Plot barplot of average effect size by diagnosis group'''
    cum_codes = ht.hypothesis_test_four(cleaned_data)
    plt.figure(figsize=(14, 7))
    sns.barplot('code', 'avg_effect', data=cum_codes, palette='deep')
    plt.xticks(rotation=90)
    plt.ylabel('Average Effect')
    plt.xlabel('Diagnosis Group')
