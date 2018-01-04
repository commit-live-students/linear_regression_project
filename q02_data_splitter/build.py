# %load q02_data_splitter/build.py
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

X,y = data_splitter(df)
print ("Testing")
print type(X)
print type(y)
print X.shape
print y.shape
print X.iloc[5,3]
print y.iloc[4]
print X.head()
print y.head()


df.head()

# Dependent variable or target is the SalePrice
# All other variables are features or independent
dep = df["SalePrice"]
indep = df.loc[:,df.columns != "SalePrice"]
print ("Dependent Variable")
print ("******************")
print dep.head()
print ("Independent Variables")
print ("*********************")
print indep.head()
