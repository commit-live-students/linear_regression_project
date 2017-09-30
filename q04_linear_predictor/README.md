## Your very first prediction - Using fitted linear regression model

Let's write a function `linear_predictor()` that takes in a fitted linear model and makes a prediction. It also calculates Mean square error, Mean absolute error and r2.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| lm | sklearn.linear_model.base.LinearRegression | Fitted Linear Regression model |
| X | DataFrame | compulsory | | Dataframe containing feature variables |
| y | Series/DataFrame | compulsory | | Target Variable |

#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| y_pred | Series | Predicted values |
| mse | float | Mean square error |
| mae | float | Mean absolute error |
| r2 | float | R-squared |
