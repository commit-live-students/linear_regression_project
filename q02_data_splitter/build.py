# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(data):
    X = data.iloc[:,:-1]
    y = data.SalePrice
    return X, y
