# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from sklearn.linear_model import LinearRegression
from statsmodels.regression.linear_model import RegressionResults
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, _, __, ___ = linear_predictor(linear_model, X, y)

def residuals(y, y_pred):

    y_pred = linear_model.predict(X)
    error_residuals = y - y_pred

    return error_residuals
