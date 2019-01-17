# %load q07_hist_residuals/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from greyatomlib.linear_regression.q05_residuals.build import residuals
import matplotlib.pyplot as plt
plt.switch_backend('agg')


dataframe = load_data('data/house_prices_multivariate.csv')



def hist_residuals(error_residuals, bins=60):
    # Create a histogram
    plt.hist(x=error_residuals, bins=bins)
    plt.title('Residuals Histogram')
    plt.xlabel('Residual Errors')
    plt.ylabel('Frequency')
    plt.show()
    return None


