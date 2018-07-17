# Linear Regression Project

We learnt about the New York house prices dataset in the in-class session. We learnt
* What is linear regression
* How gradient descent algorithm works to minimize the cost function
* What are the assumptions of linear regression

We also implemented linear regression using `sklearn` library in which we

* Fit a linear regression model
* Predicted house prices using the fitted model
* Calculated MSE for predicted and actual house prices

Now, let's take this forward and increase our understanding of linear regression!

This assignment is a series of simple tasks, in which we will be fitting a linear regression model on the house pricing data and validating some of the assumptions of linear regression.

## Why solve this assignment?

By the end of this assignment,

* You will be able to confidently train a linear regression model and predict values of the target variables
* You will have a better understanding about the assumptions of linear regression and how to validate them.
By completing this project you have an opportunity to win 800 points!!

## On assumptions of linear regression

Assumptions of linear regression model play an extremely important role in the model performance and stability. Hence, it is very important to validate these assumptions. Validating these assumptions can give us deeper insights into the **kind of data** we are dealing with and **steps that could be taken to improve the results** of the linear model.

So, let's get started.

## About House Prices dataset


Here are some of the imports that we will be using throughout the assignment.


**import pandas as pd**

**import numpy as np<br>**

**import matplotlib.pyplot as plt<br>**

**from pprint import pprint<br>**

**%matplotlib inline<br>**

**from sklearn.linear_model import LinearRegression<br>**

**from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score<br>**
