# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
import pandas as pd
df = load_data('data/house_prices_multivariate.csv')


# Your Code Here
def data_splitter(df):
    # Split into dep and indep variables (target and features)
    dep = df["SalePrice"]
    indep = df.loc[:,df.columns != "SalePrice"]
#     print ("Dependent Variable")
#     print ("******************")
#     print dep.head()
#     print ("Independent Variables")
#     print ("*********************")
#     print indep.head()
    return indep, dep

# X,y = data_splitter(df)
# print ("Testing")
# print type(X)
# print type(y)
# print X.head()
# print y.head()
