# %load q04_linear_predictor/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
lr = LinearRegression()

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)

def linear_predictor(lm,X,y):
    #lm.fit(X,y)
    y_pred = lm.predict(X)
    mse = mean_squared_error(y_pred,y)
    mae = mean_absolute_error(y_pred,y)
    r2 = r2_score(y_pred,y)
    return(y_pred,mse,mae,r2)
linear_predictor(lr,X,y)



