import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression
from q04_linear_predictor.build import linear_predictor
from q05_residuals.build import residuals
from q06_plot_residuals.build import plot_residuals
import matplotlib.pyplot as plt

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X,y)

# use residuals() and linear_predictor()


def hist_residuals(error_residuals, bins):
    '''Enter Code Here'''
    return plt
