import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from q02_data_splitter.build import data_splitter

from q01_load_data.build import load_data

class TestLoad_data(TestCase):
    def test_data_splitter(self):
        dataframe = load_data('../data/house_prices_multivariate.csv')
        X_house_prices, y_house_prices = data_splitter(dataframe)
        self.assertTrue('LotArea' in dataframe.columns.values)
        self.assertTrue('SalePrice' in dataframe.columns.values)