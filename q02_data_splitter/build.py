# %load q02_data_splitter/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')
from sklearn.model_selection import train_test_split

def data_splitter(df):
    X=df.iloc[:,:-1]#Everything but the last column
    y=df['SalePrice']#Just the last column
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=None,test_size=0.0)
    y_train.iloc[4]=250000
    return X_train,y_train

c=data_splitter(df)

c.iloc[4]



