
import pandas as pd
path = 'data/house_prices_multivariate.csv'
def load_data(path):
        return pd.read_csv(path)
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    return df.iloc[:,:-1],df.iloc[:,-1]

