from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df1):
    X= df1.iloc[:,0:-1]
    y= df1.iloc[:,-1]
    return X,y

data_splitter(df)
