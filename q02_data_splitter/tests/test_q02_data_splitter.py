from greyatomlib.linear_regression.q01_load_data.build import load_data
from ..build import data_splitter
from unittest import TestCase
from inspect import getargspec
import pandas

df = load_data('data/house_prices_multivariate.csv')
X_house_prices, y_house_prices = data_splitter(df)

class TestDataSplitter(TestCase):
    def test_data_splitter_arguments(self):

        # Input parameters tests
        args = getargspec(data_splitter)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test_data_splitter_defaults(self):
        args = getargspec(data_splitter)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")


        # Return type tests
    def test_data_splitter_dataframe_instance(self):  
        
        self.assertIsInstance(X_house_prices, pandas.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(X_house_prices)))

    def test_data_splitter_series_instance(self):
        
        self.assertIsInstance(y_house_prices, pandas.Series,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(y_house_prices)))

    def test_data_splitter_target_shape(self):
        
        self.assertEqual(y_house_prices.shape, (1379,),
                         "Return value shape does not match expected value")

    def test_data_splitter_feature_shape(self):
        
        self.assertEqual(X_house_prices.shape, (1379, 34),
                         "Return value shape does not match expected value")
    def test_data_splitter_target_return_value(self):
        
        self.assertEqual(y_house_prices.iloc[4], 250000,
                         "Return value does not match expected value")
    def test_data_splitter_feature_return_value(self):
        self.assertEqual(X_house_prices.iloc[5, 3], 5,
                         "Return value value does not match expected value")
