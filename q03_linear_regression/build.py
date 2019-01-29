# %load q03_linear_regression/build.py
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(dataframe)

# Write your code here :
def linear_regression(X,y):
    reg = LinearRegression()
    #xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)
#    reg.fit(xTrain,yTrain)
    return reg.fit(X,y)


linear_regression(X,y)

