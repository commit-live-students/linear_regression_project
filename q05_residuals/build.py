import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression
from q04_linear_predictor.build import linear_predictor
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

# call  linear_regression() and linear_predictor() function 

def residuals(y=y, y_pred=y_pred):
    # code here
    return error_residuals
