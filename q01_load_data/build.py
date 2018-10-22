import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

path = 'data/house_prices_multivariate.csv'

def load_data(path):
    
    df = pd.read_csv(path)
    return df

load_data(path)




