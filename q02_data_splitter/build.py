# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    y = df.pop('SalePrice')
    X = df
    return X,y
X , y = data_splitter(df)
print(X.iloc[5,3])
print(y.iloc[4])

