# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


def data_splitter(df):

    df['Lot Frontage']=df.index
    df.index = range(df.shape[0])
    features = list(df.columns)
    features = [features[-1]]+features[:-1]



    #target = df['SalePrice']
    #features = del list(df.columns)[len(list(df.columns))-1]
    features.remove('SalePrice')
    X = df[features]
    y = df['SalePrice']


    return X,y


# Your Code Here
