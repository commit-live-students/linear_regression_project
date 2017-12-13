from unittest import TestCase
from inspect import getargspec
import pandas
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from ..build import residuals

dataframe = load_data('data/house_prices_multivariate.csv')
X_house_prices, y_house_prices = data_splitter(dataframe)
lm = linear_regression(X_house_prices, y_house_prices)
y_pred_house_prices, _, ___, __ = linear_predictor(lm, X_house_prices, y_house_prices)
residuals_house_prices = residuals(y_house_prices, y_pred_house_prices)

class TestResiduals(TestCase):
    def test_residuals_arguments(self):

        # Input parameters tests
        args = getargspec(residuals)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
    def test_residuals_defaults(self):
        args = getargspec(residuals)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        
        
    def test_residuals_prices_instance(self):
        self.assertIsInstance(residuals_house_prices, pandas.Series,
                              "Expected data type for return value is `numpy.ndarray`, you are returning %s" % (
                                  type(residuals_house_prices)))

    def test_residuals_price_shape(self):
        # Return value tests
        self.assertEqual(residuals_house_prices.shape, (1379,), "Return `residuals` shape does not match expected value")
    def test_residuals_price_values_0(self):
        self.assertAlmostEqual(residuals_house_prices.iloc[0], -14665.2446233, 2, "Return value does not match expected value")
    def test_residuals_price_values_20(self):
        self.assertAlmostEqual(residuals_house_prices.iloc[20], 28662.5413679, 2, "Return value does not match expected value")

    def test_residuals_price_values_30(self):
        self.assertAlmostEqual(residuals_house_prices.iloc[30], -28207.3493296, 2, "Return value does not match expected value")
        