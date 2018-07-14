# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, _, __, ___ = linear_predictor(linear_model, X, y)


# Your code here
def residuals(y_test,y_pred):
    return y_test-y_pred
