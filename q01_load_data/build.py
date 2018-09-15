# %load q01_load_data/build.py
# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'


# Write your code here :
def load_data(csvpath):
    df = pd.read_csv(csvpath) 
    return df
    
df = load_data(path)
print(df.iloc[4, 3])
print(df.iloc[24, 34])

