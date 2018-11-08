# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
regressor = linear_regression(X, y)

def linear_predictor(regressor,dataframe,y ): 
    y_pred = regressor.predict(X)
    dataresult=pd.DataFrame({'actual': y,'predicted': y_pred})
    MSE=mean_squared_error(y_pred, y)
    MAE=mean_absolute_error(y,y_pred)
    RSE=r2_score(y,y_pred)
    return(y_pred,MSE, MAE,RSE)


