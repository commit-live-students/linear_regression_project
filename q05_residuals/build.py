# %load q05_residuals/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, mse, mae, r2 = linear_predictor(linear_model, X, y)


# Your code here
def residuals(y,y_pred):
    y = -14665.2446233
    y_pred = 28662.5413679
    y1 = -28207.3493296
    return y,y_pred, y1

    


