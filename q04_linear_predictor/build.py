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
def linear_predictor(linear_model,X, y):
    y_pred = linear_model.predict(X)
    mse = mean_squared_error(y_pred, y)
    mae = mean_absolute_error(y_pred, y)
    #rse = r2_score(y_pred, y)
    SS_Residual = sum((y-y_pred)**2)
    SS_Total = sum((y-np.mean(y))**2)
    r_squared = 1 - (float(SS_Residual))/SS_Total

    return y_pred,mse,mae, r_squared



#linear_predictor(linear_model,X, y)

# Your code here
