# Default Imports
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_prices_multivariate.csv', index_col=False)
def data_splitter(df) :
    #df = pd.read_csv('data/house_prices_multivariate.csv', index_col=False)

    # making Independent and Dependent variables from the dataset
    X = df.iloc[:,:-1]
    y = df.SalePrice
    #df = pd.DataFrame(np.genfromtxt(path, dtype=dt))
    #df = df.reset_index()



# Your Code Here
