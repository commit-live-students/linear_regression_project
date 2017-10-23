# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from greyatomlib.linear_regression.q05_residuals.build import residuals
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('agg')


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, _, __, ___ = linear_predictor(linear_model, X, y)
error_residuals = residuals(y, y_pred)


def hist_residuals(residuals, bins=60):
    plt.hist(residuals,bins=bins)
    plt.xlim(-490900,304999)
    plt.show()

hist_residuals(error_residuals, 60)
