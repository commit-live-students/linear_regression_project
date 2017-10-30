# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df):
    df=pd.read_csv('data/house_prices_multivariate.csv',index_col=None)
    #print(df.shape)
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1]

    return x,y

# Your Code Here
