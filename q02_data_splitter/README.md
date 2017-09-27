## Task 2: Split Data into Feature and Target Variables

Now that you have imported the data, let's split data into target or dependent variable and feature or independent variables. We can use these variables later on to fit a linear regression model.

What would be the dependent variable here?

Tip: In practice, we denote dependent variables with capital X and target variable with small y.

Let's write a function `data_splitter()` which seperates features and target variables:

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| df | DataFrame | compulsory |  | Input Dataframe to split |


#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X | DataFrame | Dataframe containing feature variables |
| y | Series/DataFrame | Target Variable |