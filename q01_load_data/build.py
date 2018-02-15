import pandas as pd

path = 'data/house_prices_multivariate.csv'

def load_data(path1):
    df1 = pd.read_csv(path1)
    return df1

load_data(path)
