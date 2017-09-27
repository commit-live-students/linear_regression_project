import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter

from sklearn.linear_model import LinearRegression

def linear_regression(X, y):
    linear_regressor = LinearRegression(normalize=False)
    linear_regressor.fit(X, y)
    return linear_regressor