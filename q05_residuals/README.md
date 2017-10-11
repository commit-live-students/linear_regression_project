# Calculating residuals - Residuals reveal the real story

## Let's write a function `residuals()` that
* Takes in original target variable and our predictions and calculates the residuals.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| y | Series/DataFrame | compulsory | | Target Variable |
| y_pred | Series/DataFrame | compulsory | | Predicted Values |

#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| error_residuals | Series | Residuals |
