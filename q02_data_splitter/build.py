# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

# Your Code Here
def data_splitter(df):
    print(len(df.columns)-1)
    X = df.iloc[:,:len(df.columns)-1]
    print(X.shape)
    y = df['SalePrice']
    print(y.shape)
    return(X,y)
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')
data_splitter(df)


