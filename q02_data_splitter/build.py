# Default Imports
#from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = pd.read_csv('/home/darshind/Workspace/code/linear_regression_project/data/house_prices_multivariate.csv',engine='python')


# Your Code Here
def data_splitter(df):
            X = df.drop('SalePrice',axis = 1)
            y = df['SalePrice']
            return X,y
print data_splitter(df)
