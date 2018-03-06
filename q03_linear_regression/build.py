from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)
def linear_regression(X,y):
    lm = lr.fit(X,y)
    return lm
#print fit_line
