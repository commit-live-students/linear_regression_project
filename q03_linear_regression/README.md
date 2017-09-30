## Fitting your first linear regression model

Let's write a function `linear_regression()` which takes as input the features and target and fits a LinearRegression with default parameters model on it.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | DataFrame | compulsory | | Dataframe containing feature variables |
| y | Series/DataFrame | compulsory | | Target Variable |


#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| lm | sklearn.linear_model.base.LinearRegression | Fitted Linear Regression model |
