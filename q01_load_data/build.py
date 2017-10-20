# %load q01_load_data/build.py
# Default imports
import pandas as pd
import numpy as np


path = 'data/house_prices_multivariate.csv'


# Your code here
def load_data(path):
    data = pd.read_csv(path)

    return data

load_data(path)
