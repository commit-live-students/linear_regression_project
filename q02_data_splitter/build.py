# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

# Your Code Here
def data_splitter(data):
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    
    return X, y

feature, target = data_splitter(df)
print(feature.shape)
print(target.shape)
print(target.iloc[4])
print(feature.iloc[5, 3])

