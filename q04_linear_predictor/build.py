# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)

def linear_predictor(linear_model,X,y):
    y_pred = linear_model.predict(X)
    mean_square_err=mean_squared_error(y_pred, y)
    mean_abs_err=mean_absolute_error(y_pred,y)
    r_sqr=r2_score(y,y_pred)
    return y_pred,mean_square_err,mean_abs_err,r_sqr


