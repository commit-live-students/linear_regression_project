# Default imports
import pandas as pd

path = 'data/house_prices_multivariate.csv'



def load_data(path):
    

    data = pd.read_csv(path , index_col= False)

    return data

load_data(path)
