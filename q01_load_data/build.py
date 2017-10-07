# Defualt imports
import pandas as pd
import numpy as np

# Your solution
def load_data(path):
    dataframe = pd.read_csv(path)
    return  dataframe
