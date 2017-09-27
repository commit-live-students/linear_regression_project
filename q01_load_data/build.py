import pandas as pd

def load_data(path):
    dataframe = pd.read_csv(path,index_col=0)
    return  dataframe