# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'

# Write your code here :
def load_data(path):
    datafr = pd.read_csv(path)
    #datafr.drop(columns = ['#'])
    #print (datafr)
    #print (datafr.iloc[24, 34])
    return datafr

#load_data(path)




