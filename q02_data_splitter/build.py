# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df):

    # Dependent variable
    y = df.iloc[:,-1]
    # Independent variable
    X = df.iloc[:,:-1]

    return X, y
