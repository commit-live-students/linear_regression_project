# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    X = df.iloc[:,:-1] #all columns except the last one
    #y = df.iloc[:,len(df[0])-1] #only the last column
    y = df.iloc[:,-1]
    return X,y
    

data_splitter(df)
#data_splitter(df)
#df.head()
y = df.iloc[:,-1]
y

