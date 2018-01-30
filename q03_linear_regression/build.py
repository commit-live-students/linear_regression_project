# %load q03_linear_regression/build.py
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.2f}'.format
np.disp.float_format = '{:.10f}'.format

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

def linear_regression(X,y):
    
    regressor = LinearRegression()
    return regressor.fit(X, y)

print linear_regression(X,y)
#print('intercept:', regressor.intercept_)
#print('coefficients of predictors:', regressor.coef_[33])

