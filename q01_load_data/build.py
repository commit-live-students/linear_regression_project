# Default imports
import pandas as pd
import numpy as np
def load_data(path) :

    df = pd.read_csv(path, index_col=False)
    #df = pd.DataFrame(np.genfromtxt(path, dtype=dt))
    #df = df.reset_index()

    return df

#load_data ('data/house_prices_multivariate.csv', str)


# Your code here
