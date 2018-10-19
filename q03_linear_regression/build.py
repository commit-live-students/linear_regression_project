# %load q03_linear_regression/build.py
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter

import pandas as pd 

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

def linear_regression(X,y):
    #df=dataframe
    from sklearn.linear_model import LinearRegression
    lin_reg=LinearRegression()
    lin_reg.fit(X,y)
    return lin_reg
    


    
    
    
    
    
    
    
    
linear_regression(X,y)




