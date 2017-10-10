from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression

# Load the package for linear regression and use load_data() and data_splitter() function
dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)


def linear_regression(X, y):
    # Enter your code
    linear_regressor = LinearRegression(normalize=False)
    linear_regressor.fit(X, y)
    return linear_regressor
