# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


def data_splitter(df):
    X = df.iloc[:,0:-1]
    y = df.iloc[:,-1]
    return X,y
X, y = data_splitter(df)
