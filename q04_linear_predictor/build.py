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




# Your code here
def linear_predictor(lm,X,y):
    linearRegressor = LinearRegression(normalize = False)
    ypred = linear_model.predict(X)
    mse = mean_squared_error(y,ypred)
    r2 = r2_score(y, ypred)
    mae = mean_absolute_error(y, ypred)
    return ypred,mse,mae,r2
linear_predictor(linear_model,X,y)


