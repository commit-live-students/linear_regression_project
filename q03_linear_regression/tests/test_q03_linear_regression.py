import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from q03_linear_regression.build import linear_regression

from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter

class TestLoad_data(TestCase):
    def test_linear_regression(self):

        dataframe = load_data('../data/house_prices_multivariate.csv')
        X_house_prices, y_house_prices = data_splitter(dataframe)
        lm = linear_regression(X_house_prices, y_house_prices)
        self.assertTrue(lm.coef_.shape[0], 34)