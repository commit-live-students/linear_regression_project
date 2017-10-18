# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')
df.head()
def data_splitter(df):
#y = df.loc[:,'SalePrice']
    X = df.iloc[:,:-1]
    y = df.SalePrice



    return X, y



# Your Code Here
