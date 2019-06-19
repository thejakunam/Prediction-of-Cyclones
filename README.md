# Prediction-of-Cyclones
Predicting Cyclones using Time Series Forecasting Models and further Categorizing it.
Data Set contains Wind Speed and Pressure Values(Source : NOAA), on which data preprocessing has been done to handle missing values and outliers.Further, unnecesary attributes are removed.
Data Normalization Techniques like min-max and Z-score are carried out to scale down the values to a specific range.
Data is now fed to Time Series Forecasting models like Naive Forecast, Period Moving Average, Linear Regression and 4th order Polynomial Regression
Accuracy measures like Scatter index, RMSE and correlation are calculated to find the best model.

For any model that works best, RMSE values will be less and correlation (i.e. correlation between predicted and observed values) should be near to 1 or equal to 1. 

In majority of cases, Regression seemed to be performing better. However, Poly Regression model has given good results in two cases and so can be considered as the next best model.


Some Limitations include:
Haven’t used information regarding latitudes and longitudes in forecasting process. 
Though min-max normalization seems to be giving better results, there is one exception in one station.
Though Regression is identified as best model, doesn’t give best results in all cases.
