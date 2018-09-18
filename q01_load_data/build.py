# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'

def load_data(path):
    data_1=pd.read_csv(path)
    #data=data_1.set_index(['LotFrontage'], inplace=True)
    return data_1

# Write your code here :






