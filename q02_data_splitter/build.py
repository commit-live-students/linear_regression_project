# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


def data_splitter(df):
    return df.loc[:, df.columns != 'SalePrice'], df[ 'SalePrice']


data_splitter(df)


