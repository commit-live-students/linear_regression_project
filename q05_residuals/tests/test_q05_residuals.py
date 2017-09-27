import sys, os
import pandas
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from q05_residuals.build import residuals


from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression
from q04_linear_predictor.build import linear_predictor


class TestLoad_data(TestCase):
    def test_residuals(self):


        dataframe = load_data('../../data/house_prices_multivariate.csv')
        X_house_prices, y_house_prices = data_splitter(dataframe)
        lm = linear_regression(X_house_prices, y_house_prices)
        y_pred_house_prices, mse_house_prices, mae_house_prices, r2_house_prices = linear_predictor(lm, X_house_prices,
                                                                                                    y_house_prices)


        residuals_house_prices = residuals(y_house_prices, y_pred_house_prices)
        self.assertAlmostEqual(residuals_house_prices.iloc[0], -14416.966735, places=2)
        self.assertAlmostEqual(residuals_house_prices.iloc[1], -10609.336208, places=2)
        self.assertAlmostEqual(residuals_house_prices.iloc[2], 7823.704216, places=2)
        self.assertAlmostEqual(residuals_house_prices.iloc[3], -57568.429095, places=2)
        self.assertAlmostEqual(residuals_house_prices.iloc[4], -44649.076922, places=2)