# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from greyatomlib.linear_regression.q05_residuals.build import residuals
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, _, __, ___ = linear_predictor(linear_model, X, y)
error_residuals = residuals(y, y_pred)


# Your code here
def plot_residuals(y, error_residuals):
    # Create a scatter plot to compare residual values against dep variable
    plt.scatter(y, error_residuals)
    plt.title("Residuals plot")
    plt.xlabel("Sale Price")
    plt.ylabel("Errors")
    plt.show()
    return None

# plot_residuals(y, error_residuals)
