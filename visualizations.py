"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from hypothesis_tests import create_sample_dists
from hypothesis_tests import get_sample_means


# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

def plot_distribution_means(cleaned_data,y_var=None,categories = []):

    # Get data for tests
    comparison_groups = comparison_groups = create_sample_dists(cleaned_data, y_var='average_covered_charges', categories=['metro','non_metro'])

    ###
    
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    
    metro_means = get_sample_means(comparison_groups[0],100)
    non_metro_means = get_sample_means(comparison_groups[1],100)
   
    sns.distplot(metro_means, label=str(categories[0]))
    sns.distplot(non_metro_means , label=str(categories[1]))
    plt.legend()




def plot_distribution(cleaned_data,y_var=None,categories = []):

    # Get data for tests
    comparison_groups = comparison_groups = create_sample_dists(cleaned_data, y_var='average_covered_charges', categories=['metro','non_metro'])

    ###
    
    metro_sample = comparison_groups[0]
    non_metro_sample = comparison_groups[1]
        
    sns.distplot(metro_sample, label=str(categories[0]))
    sns.distplot(non_metro_sample , label=str(categories[1]))
    plt.legend()
    

def overlapping_density(package=None, input_vars=None, target_vars=None):
    """
    Set the characteristics of your overlapping density plot
    All arguments are set to None purely as a filler right now

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    Should be able to call this function in later visualization code.

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any other value should throw and error
    :param input_vars:     should take the x variables/categories you want to plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization functions
    """

    # Set size of figure
    fig = plt.figure(figsize=(16, 10), dpi=80)

    # Starter code for figuring out which package to use
    if package == "sns":
        for variable in input_vars:
            sns.kdeplot(...)
    elif package == 'matplotlib':
        for variable in input_vars:
            plt.plot(..., label=None, linewidth=None, color=None, figure = fig)

    return fig



def boxplot_plot(package=None, input_vars=None, target_vars=None):
    """
    Same specifications and requirements as overlapping density plot

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any other value should throw and error
    :param input_vars:     should take the x variables/categories you want to plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization functions
    """
    plt.figure(figsize=(16, 10), dpi=80)

    pass


def visualization_one(target_var = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    # Main chunk of code here
    ###

    # Starter code for labeling the image
    plt.xlabel(None, figure = fig)
    plt.ylabel(None, figure = fig)
    plt.title(None, figure= fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
    return fig


# please fully flesh out this function to meet same specifications of visualization one

def visualization_two(output_image_name):
    pass

def visualization_three(output_image_name):
    pass

def visualization_four(output_image_name):
    pass