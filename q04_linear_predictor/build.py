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
def linear_predictor(linear_model,X,y):
    y_prediction=linear_model.predict(X)
    meansqrerror=mean_squared_error(y,y_prediction)
    meanabserror=mean_absolute_error(y,y_prediction)
    r2scoreis=r2_score(y,y_prediction)
    #print(type(y_prediction))
    #print(meanabserror)
    #print(r2scoreis)
    return y_prediction,meansqrerror,meanabserror,r2scoreis
   
# Your code here
