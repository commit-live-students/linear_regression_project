# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    #feature variable having all values except SalePrice
   
    #Target variable only sale Price
    y = df.iloc[:,-1]
    X = df.loc[:,df.columns != 'SalePrice']
    return X,y
data_splitter(df)


