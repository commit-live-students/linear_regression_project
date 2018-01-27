# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
from sklearn.svm import LinearSVC
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df):
    y = df['SalePrice']
    del df['SalePrice']
    X = df
    return X,y

print data_splitter(df)

