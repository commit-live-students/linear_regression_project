from unittest import TestCase
from ..build import linear_regression
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from inspect import getargspec


class TestLinearRegression(TestCase):
    def test_linear_regression(self):
        # Input parameters tests
        args = getargspec(linear_regression)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        dataframe = load_data('data/house_prices_multivariate.csv')
        X_house_prices, y_house_prices = data_splitter(dataframe)

        # Return value tests
        lm = linear_regression(X_house_prices, y_house_prices)
        self.assertTrue(lm.coef_.shape[0], 34)
