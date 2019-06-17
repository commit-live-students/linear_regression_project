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
def linear_predictor(lr,X_test,Y_test):
    y_pred=  lr.predict(X_test)
    mse=mean_squared_error(Y_test,y_pred)
    msa=mean_absolute_error(Y_test,y_pred)
    r2=r2_score(Y_test,y_pred)
    return y_pred,mse,msa,r2
