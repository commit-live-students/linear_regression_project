# %load q03_linear_regression/build.py
# Default Imports
import pandas as pd
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression


# Load the package for linear regression and use load_data() and data_splitter() function
df = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(df)


# Your code here

def  linear_regression(X,y):
    lm = LinearRegression()
    lm.fit(X,y)
    return lm
#print linear_regression(X,y)
