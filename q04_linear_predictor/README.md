## Your very first prediction - Using fitted linear regression model

Let's write a function `linear_predictor()` that takes in a fitted linear model and makes a prediction. It also calculates Mean square error, Mean absolute error and r2.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| lm | sklearn.linear_model.LinearRegression | compulsory | | Fitted Linear Regression model |
| X | Pandas DataFrame | compulsory | | Dataframe containing feature variables |
| y | Pandas Series | compulsory | | Target Variable |

#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| y_pred | numpy.ndarray | Predicted values |
| mse | numpy.float64 | Mean square error |
| mae | numpy.float64 | Mean absolute error |
| r2 | numpy.float64 | R-squared |
