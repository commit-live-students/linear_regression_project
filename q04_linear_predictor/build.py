# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
import numpy as np

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
lm = linear_regression(X, y)


# You(r code here
def linear_predictor(lm, X, y):
    
    y_pred = lm.predict(X)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y,y_pred)
    y_mean = y.mean()
    
    r2 = sum((y_pred - y_mean) ** 2)/sum((y - y_mean) ** 2)

    return y_pred, mse, mae, r2
     
    

linear_predictor(lm, X, y)



