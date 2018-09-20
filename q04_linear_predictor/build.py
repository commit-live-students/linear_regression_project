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
def linear_predictor(linear_model, X, y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    y_pred = regressor.predict(X)
    mse= mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)  
    return y_pred, mse, mae, r2
    
from unittest import TestCase
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from inspect import getfullargspec
import numpy
dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
lr = linear_regression(X, y)
y_pred, mse, mae, r2 = linear_predictor(lr, X, y)


class TestLinearPrediction(TestCase):
    def test_linear_predictor_arguements(self):

        # Input parameters tests
        args = getfullargspec(linear_predictor)
        self.assertEqual(len(args[0]), 3, 'Expected argument(s) %d, Given %d' % (3, len(args[0])))
    def test_linear_predictor_defaults(self):
        args = getfullargspec(linear_predictor)
        self.assertEqual(args[3], None, 'Expected default values do not match given default values')

        # Return type tests
    def test_linear_regression_target_instance(self):    
        self.assertIsInstance(y_pred, numpy.ndarray,
                              'Expected data type for return value is , you are returning %s' % (
                                  type(y_pred)))
    def test_linear_regression_metric_mse_instance(self):
        self.assertIsInstance(mse, numpy.float64,
                              'Expected data type for return value is , you are returning %s' % (
                                  type(mse)))
    def test_linear_regression_metric_mae_instance(self):
        self.assertIsInstance(mae, numpy.float64,
                              'Expected data type for return value is , you are returning %s' % (
                                  type(mae)))
    def test_linear_regression_metric_r2_instance(self):
        self.assertIsInstance(r2, numpy.float64,
                              'Expected data type for return value is , you are returning %s' % (
                                  type(r2)))
    def test_linear_regression_pred_shape(self):
        # Return value tests
        self.assertEqual(y_pred.shape, (1379,), 'Return  shape does not match expected value')

    def test_linear_regression_pred_value_0(self):
        self.assertAlmostEqual(y_pred[0], 223165.244623, 2, 'Return value does not match expected value')

    def test_linear_regression_pred_value_20(self):
        self.assertAlmostEqual(y_pred[20], 296637.458632, 2, 'Return value does not match expected value')
    
    def test_linear_regression_mse_value(self):
        self.assertAlmostEqual(mse, 1219044781.49, 2, 'Return value does not match expected value')
    def test_linear_regression_mae_value(self):
        self.assertAlmostEqual(mae, 21224.300871, 2, 'Return value does not match expected value')
    def test_linear_regression_r2_value(self):
        self.assertAlmostEqual(r2, 0.80464798594, 2, 'Return value does not match expected value')



