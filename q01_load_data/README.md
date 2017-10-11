# Let's get going - Load Data

We will start with loading the data into a variable, which we will use for further analysis

## write a function `load_data()` that 

* Loads a dataset using panda's read_csv api with the following specifications:

**Notice that you need to drop the index column.**

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path to the file csv |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| df | Pandas DataFrame | DataFrame for creating our model |
