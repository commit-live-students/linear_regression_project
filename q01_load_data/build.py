# Default imports
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

path = 'data/house_prices_multivariate.csv'



def load_data(path):
    data = pd.read_csv(path)
    return data
