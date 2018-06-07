# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here

def data_splitter(df):    
    y_house_price=df.iloc[:,-1]
    x_house_price=df.iloc[:,:-1]
    return x_house_price, y_house_price

