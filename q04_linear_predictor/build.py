# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)


# Your code here
def linear_predictor(linear_model,X,y):
    y_predict = linear_model.predict(X)
    y_mse = mean_squared_error(y,y_predict)
    y_mae = mean_absolute_error(y,y_predict)
    y_r2 = r2_score(y,y_predict)
    return y_predict, y_mse, y_mae, y_r2
linear_predictor(linear_model,X,y)


