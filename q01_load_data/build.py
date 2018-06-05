# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'


# Write your code here :
def load_data(path):
    df=pd.read_csv('data/house_prices_multivariate.csv',index_col=None)
    df.reset_index(drop=True,inplace=True)
    return df

#df=load_data(path)
#df


