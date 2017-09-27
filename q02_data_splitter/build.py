import pandas
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from q01_load_data.build import load_data

def data_splitter(df):
    dataframe = load_data('../../data/house_prices_multivariate.csv')
    if type(dataframe) == pandas.DataFrame:
        print("True")
    else:
        print("False")
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    return X, y