# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression


# Load the package for linear regression and use load_data() and data_splitter() function
df = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(df)


# df['Lot Frontage']=df.index
# df.index = range(df.shape[0])
# features = list(df.columns)
# features = [features[-1]]+features[:-1]
# features.remove('SalePrice')
#
# y = df['SalePrice']
# X = df[features]
#y= df['SalePrice']
#X
#import numpy as np
def linear_regression(X,y):
    model = LinearRegression()
    model.fit(X,y)
    return model

#print(model)

# Your code here
