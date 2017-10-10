from unittest import TestCase
from ..build import linear_predictor
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from inspect import getargspec
import numpy


class TestLinearPrediction(TestCase):
    def test_linear_predictor(self):

        # Input parameters tests
        args = getargspec(linear_predictor)
        self.assertEqual(len(args[0]), 3, "Expected argument(s) %d, Given %d" % (3, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return type tests
        dataframe = load_data('data/house_prices_multivariate.csv')
        X, y = data_splitter(dataframe)
        lr = linear_regression(X, y)
        y_pred, mse, mae, r2 = linear_predictor(lr, X, y)

        self.assertIsInstance(y_pred, numpy.ndarray,
                              "Expected data type for return value is `numpy.ndarray`, you are returning %s" % (
                                  type(y_pred)))
        self.assertIsInstance(mse, numpy.float64,
                              "Expected data type for return value is `numpy.float64`, you are returning %s" % (
                                  type(mse)))
        self.assertIsInstance(mae, numpy.float64,
                              "Expected data type for return value is `numpy.float64`, you are returning %s" % (
                                  type(mae)))
        self.assertIsInstance(r2, numpy.float64,
                              "Expected data type for return value is `numpy.float64`, you are returning %s" % (
                                  type(r2)))

        # Return value tests
        self.assertEqual(y_pred.shape, (1379,), "Return `y_pred` shape does not match expected value")
        self.assertAlmostEqual(y_pred[0], 223165.244623, 2, "Return value does not match expected value")
        self.assertAlmostEqual(y_pred[20], 296637.458632, 2, "Return value does not match expected value")
        self.assertAlmostEqual(y_pred[40], 143009.698988, 2, "Return value does not match expected value")
        self.assertAlmostEqual(y_pred[80], 117414.018664, 2, "Return value does not match expected value")
        self.assertAlmostEqual(mse, 1219044781.49, 2, "Return value does not match expected value")
        self.assertAlmostEqual(mae, 21224.300871, 2, "Return value does not match expected value")
        self.assertAlmostEqual(r2, 0.80464798594, 2, "Return value does not match expected value")
