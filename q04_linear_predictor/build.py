# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)

y_len=len(y)

# Your code here

def linear_predictor(lm,X,y):
    lr= linear_regression()
    y_pred=lr.predict(X)
    mse=mean_squared_error(y_pred, y)
    mae=mean_absolute_error(y_pred,y)
    sst=0
    ssr=0
    for i in range(y_len):
        sst = sst+(y[i] - y.mean())**2
        ssr = ssr+(y_pred[i] - y.mean())**2
    r2=ssr/sst
    return y_pred,mse,mae,r2
