# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df):
    X= df.loc[:, df.columns != 'SalePrice']
    y = df.iloc[:,-1]
    return X, y

data_splitter(df)



