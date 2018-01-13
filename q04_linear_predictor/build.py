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
import numpy as np

def linear_predictor(lm,X,y):
    y_pred = lm.predict(X)
    n= len(y)
    sse = np.float64( ((y- y_pred)**2).sum() )
    mse = np.float64( sse/n)
    mae = np.float64( (abs(y- y_pred)).sum()/n  )
    sst = ((y-y.mean())**2).sum()
    r2= np.float64(  1 - (sse/sst))
    return y_pred ,mse,mae, r2

y_pred,mse,mae,r2 = linear_predictor(linear_model,X,y)

#print 'mae : ' , mae
#print 'mse : ' , mse
#print 'r2 : ',r2
