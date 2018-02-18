# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    dfX = df.iloc[:,:-1]
    dfy = df['SalePrice']
    return dfX, dfy
