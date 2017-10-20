# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
import numpy as np
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    y=df.SalePrice
    X=df.iloc[:,:-1]
    #print(y)
    return X,y

# x,y=data_splitter(df)


# print(y.shape)
# print(x.shape)
# print(y.iloc[4])
# print(x.iloc[5,3])

# if isinstance(x,pd.DataFrame):
#     print('Yes')

# if isinstance(y, pd.Series):
#     print('Yes')
