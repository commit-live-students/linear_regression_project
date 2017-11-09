# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'


# Your code here
def load_data(path):
    data = pd.read_csv(path,index_col=False)
    return data
