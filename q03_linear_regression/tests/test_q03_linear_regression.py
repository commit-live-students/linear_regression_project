from unittest import TestCase
from ..build import linear_regression
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from inspect import getargspec
import sklearn.linear_model


class TestLinearRegression(TestCase):
    def test_linear_regression(self):

        # Input parameters tests
        args = getargspec(linear_regression)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        dataframe = load_data('data/house_prices_multivariate.csv')
        X, y = data_splitter(dataframe)
        lr = linear_regression(X, y)
        self.assertIsInstance(lr, sklearn.linear_model.LinearRegression,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(lr)))

        # Return value tests
        self.assertEqual(lr.coef_.shape, (34,), "Return value shape does not match expected value")
        self.assertAlmostEqual(lr.coef_[3], 5845.97164192, 4, "Return value does not match expected value")
        self.assertAlmostEqual(lr.coef_[5], 119.385237246, 4, "Return value does not match expected value")
        self.assertAlmostEqual(lr.coef_[10], 9.87201953507, 4, "Return value does not match expected value")
        self.assertAlmostEqual(lr.coef_[33], -583.097021217, 4, "Return value does not match expected value")
        self.assertAlmostEqual(lr.intercept_, 310649.260089, 4, "Return value does not match expected value")
