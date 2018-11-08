# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd

df = load_data('data/house_prices_multivariate.csv')
def data_splitter(df):
    y=df.iloc[:,]
    x=df.iloc[:,0:34]
    return(x,y)
data_splitter(df)

