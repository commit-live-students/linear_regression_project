# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)

def linear_predictor(linear_model, X, y):
    #print('intercept:', linear_model.intercept_)
    #print('coefficients of predictors:', linear_model.coef_)
    my_house = X.iloc[155]
    #my_house
    pred_my_house = linear_model.predict(my_house.reshape(1, -1))
    #print('predicted value:', pred_my_house[0])
    #print('actual value:', y[155])
    # Predicting the results
    y_pred = linear_model.predict(X)
    #y_pred[:10]
    #prices = pd.DataFrame({'actual': y,'predicted': y_pred})
    #prices.head(10)
    mse = mean_squared_error(y_pred, y)
    mae = mean_absolute_error(y_pred, y)
    r2 = r2_score(y, y_pred)
    return y_pred, mse, mae, r2

print linear_predictor(linear_model, X, y)

