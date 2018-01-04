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
def linear_predictor(lm, X, y):
    # Using the linear regression object lm, prdict y value
    y_pred = lm.predict(X)

    # We need to use the predicted and actual values of y
    # to calculate MAE and MSE values
    # Adding the predicted value into the original data frame
    # Here SalePrice is the actual value
    dataframe["SalePricePredicted"] = lm.predict(X)

    # We can now use these two columns to calculate the errors
    mse = mean_squared_error(dataframe["SalePrice"], dataframe["SalePricePredicted"])

    mae = mean_absolute_error(dataframe["SalePrice"], dataframe["SalePricePredicted"])

    r2 = r2_score(dataframe["SalePrice"], dataframe["SalePricePredicted"])

    # Voila
    return y_pred, mse, mae, r2



y, mse, mae, r2 = linear_predictor(linear_model, X, y)
print {"##### Testing #####"}
print "Predicted Y value type: {0}".format(type(y))
print "Predicted Y value: {0}".format(y)

# Print out the errors for testing
print "Mean Squared Error: {0}".format(mse)
print "MSE Type: {0}".format(type(mse))
print "Mean Absolute Error: {0}".format(mae)
print "MAE Type: {0}".format(type(mae))
print "R Squared Score : {0}".format(r2)
print "R2 Type: {0}".format(type(r2))


# Using the linear regression object lm, prdict y value
y = linear_model.predict(X)
print type(y)
print y.shape
print y
print y[0]
print y[20]


# We need to use the predicted and actual values of y
# to calculate MAE and MSE values
# Adding the predicted value into the original data frame
dataframe.head()

# Here SalePrice is the actual value
# dataframe["SalePricePredicted"] = linear_model.predict(X)

# We can now use these two columns to calculate the errors
mse = mean_squared_error(dataframe["SalePrice"], dataframe["SalePricePredicted"])
print "Mean Squared Error: {0}".format(mse)

mae = mean_absolute_error(dataframe["SalePrice"], dataframe["SalePricePredicted"])
print "Mean Absolute Error: {0}".format(mae)

r2 = r2_score(dataframe["SalePrice"], dataframe["SalePricePredicted"])
print "R Squared Score : {0}".format(r2)
