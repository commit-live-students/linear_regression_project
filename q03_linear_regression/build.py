# %load q03_linear_regression/build.py
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

# Write your code here :
def linear_regression(feature, target):
    lm = LinearRegression()
    lm.fit(X, y)
    
    return lm

lr = linear_regression(X, y)
print(lr.coef_.shape)
print(lr.coef_[3])
print(lr.coef_[5])
print(lr.coef_[10])
print(lr.coef_[33])
print(lr.intercept_)

