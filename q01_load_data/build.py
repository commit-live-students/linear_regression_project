# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'



def load_data(path):
    df = pd.read_csv(path)
    return df
