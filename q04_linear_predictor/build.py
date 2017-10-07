from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

# call the Linear regression function


def linear_predictor(linear_model, X, y):
    # Enter Code Here
    
    return y_pred, mse, mae, r2
