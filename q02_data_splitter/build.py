# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    y_house_prices = df.SalePrice
    X_house_prices = df[df.columns[:34]]
    return X_house_prices, y_house_prices



