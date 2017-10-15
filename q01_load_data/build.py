# Default imports
import pandas as pd

path = '/home/darshind/Workspace/code/linear_regression_project/data/house_prices_multivariate.csv'


# Your code here
def load_data(path):
    df = pd.read_csv(path)
    df.index.name = None
    df.head()
    return df
print load_data(path)
