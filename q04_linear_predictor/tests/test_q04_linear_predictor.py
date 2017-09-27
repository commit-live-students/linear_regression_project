import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from q04_linear_predictor.build import linear_predictor

from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression


class TestLoad_data(TestCase):
    def test_linear_predictor(self):

        dataframe = load_data('../../data/house_prices_multivariate.csv')
        X_house_prices, y_house_prices = data_splitter(dataframe)
        lm = linear_regression(X_house_prices, y_house_prices)

        y_pred_house_prices, mse_house_prices, mae_house_prices, r2_house_prices = linear_predictor(lm, X_house_prices,y_house_prices)
        self.assertAlmostEqual(mse_house_prices, 1220907901.18, places=2)
        self.assertAlmostEqual(mae_house_prices, 21303.706257, places=2)
        self.assertAlmostEqual(r2_house_prices, 0.804349420876, places=2)