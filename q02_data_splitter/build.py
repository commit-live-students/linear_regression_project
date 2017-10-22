# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


def data_splitter(df):
    features = df.columns.tolist()[:-1]
    X = df[features]
    y=df['SalePrice']
    return X,y



# Your Code Here
