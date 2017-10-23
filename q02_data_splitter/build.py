from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')

def data_splitter(df) :
    #df = pd.read_csv('data/house_prices_multivariate.csv', index_col=False)

    # making Independent and Dependent variables from the dataset
    X = df.iloc[:,:-1]
    y = df.SalePrice
