# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')
from sklearn.model_selection import train_test_split


# Your Code Here
def data_splitter(data):
    y = df.pop('SalePrice')
    X = df
    return X, y
