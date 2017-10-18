# Default Imports
# %load q03_linear_regression/build.py
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression
# Load the package for linear regression and use load_data() and data_splitter() function
df = load_data('data/house_prices_multivariate.csv')
df.reset_index(inplace=True)
X, y = data_splitter(df)

def linear_regression(X,y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor
