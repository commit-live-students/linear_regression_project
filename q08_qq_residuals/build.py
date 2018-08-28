# %load q08_qq_residuals/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from greyatomlib.linear_regression.q03_linear_regression.build import linear_regression
from greyatomlib.linear_regression.q04_linear_predictor.build import linear_predictor
from greyatomlib.linear_regression.q05_residuals.build import residuals
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.switch_backend('agg')

import pylab
import scipy.stats as stats


dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
linear_model = linear_regression(X, y)
y_pred, _, __, ___ = linear_predictor(linear_model, X, y)
error_residuals = residuals(y, y_pred)


# Your code here
def qq_residuals(resid):
    x = pd.DataFrame(np.random.normal(0,1,1000))
    y = pd.DataFrame(resid)
    xq = pd.qcut(x[0],100,labels=np.arange(100))
    yq = pd.qcut(y[0],100,labels=np.arange(100))
    plt.scatter(xq.sort_values(),yq.sort_values())
    

