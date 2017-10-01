import pandas

from unittest import TestCase
from q01_load_data.build import load_data

class TestLoad_data(TestCase):
    def test_load_data(self):
        dataframe = load_data('data/house_prices_multivariate.csv')
        self.assertTrue(isinstance(dataframe, pandas.DataFrame))