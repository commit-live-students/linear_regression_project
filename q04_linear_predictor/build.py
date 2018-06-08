# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import math


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
# Your code here
def linear_predictor(linear_model,X,y):
    y_pred = linear_model.predict(X)
    #print(np.array(y_pred))

    error = y.values - y_pred
    n = len(y)
    #mae = (np.sum(np.absolute(error)))/n
    #mse = math.sqrt((np.sum(error**2))/n)
    mae = mean_absolute_error(y.values,y_pred)
    mse = mean_squared_error(y.values,y_pred)
    r2 = r2_score(y.values,y_pred)
    #print(mae)
    #print(mse)
    #print(r2)
    
    return y_pred,mse,mae,r2

#linear_predictor(linear_model,X,y)

