from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
import numpy as np
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df):
    
    data = df
    y = data.SalePrice
    X = data.iloc[:,:-1]
    
    return X, y

data_splitter(df)




