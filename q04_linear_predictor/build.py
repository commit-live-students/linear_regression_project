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



def linear_predictor(lm, X, y):
    y_pred = lm.predict(X)

    dataframe['SalePricePredicted'] = lm.predict(X)

    mse = mean_squared_error(dataframe['SalePrice'], dataframe['SalePricePredicted'])

    mae = mean_absolute_error(dataframe['SalePrice'], dataframe['SalePricePredicted'])

    r2 = r2_score(dataframe['SalePrice'], dataframe['SalePricePredicted'])

    return y_pred, mse, mae, r2



 # y, mse, mae, r2 = linear_predictor(linear_model, X, y)
# print {'##### Testing #####'}
# print 'Predicted Y value type: {0}'.format(type(y))
# print 'Predicted Y value: {0}'.format(y)
#
# # Print out the errors for testing
# print 'Mean Squared Error: {0}'.format(mse)
# print 'MSE Type: {0}'.format(type(mse))
# print 'Mean Absolute Error: {0}'.format(mae)
# print 'MAE Type: {0}'.format(type(mae))
# print 'R Squared Score : {0}'.format(r2)
# print 'R2 Type: {0}'.format(type(r2))


