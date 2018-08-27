# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    t = list(df.columns.values)
    x = df[t[0:len(t)-1]]
    y = df.SalePrice
    return x,y
    pass


