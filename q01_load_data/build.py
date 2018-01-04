# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'

def load_data(path):
    return pd.read_csv(path)

data = load_data(path)
print type(data)
data

# Testing
print (data.iloc[4,3])
print (data.iloc[24,34])
