# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'


def load_data(path):
    df=pd.read_csv(path, index_col = False)
    return(df)

load_data(path)
