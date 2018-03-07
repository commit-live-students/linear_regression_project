# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
from sklearn.linear_model import LinearRegression
df = load_data('data/house_prices_multivariate.csv')

# Your Code Here
def data_splitter(df):
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1]
    return X,Y

data_splitter(df)
