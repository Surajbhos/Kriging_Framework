**Framework for Spatial Interpolation of data points**

Framework contains functionalities like Clustering, Kriging, Geohashing and Concatenating files. All these functionalities are assembled in one Python code. Kriging is a geostatistical technique used for estimating values of environmental variables at unknown locations with the help of values at known locations. Kriging technique also provides error in prediction which is known as Kriging variance.

**Steps:**

● Creates Clusters from given data

● Perform Kriging and geohashing operations on the clusters

● Estimates value of PM2.5 at each data point within 2D grid and also calculates

estimation error

● Concatenates dataframes into one file which is suitable for storing in Database

Framework consists Three Clustering methods.

● Gaussian Mixture Model Clustering 

● Fuzzy C-Means Clustering

● K-Means Clustering

It contains support for two Kriging methods.

1\. Ordinary Kriging with 5 different variograms

  ➢ Linear

  ➢ Gaussian 
  
  ➢ Spherical 
  
  ➢ Exponential 
  
  ➢ Power

2\. Universal Kriging with 5 different variograms and 1 drift parameter

   Variogram Models Linear drift parameter for linear directional trend

   ➢ Linear

   ➢ Gaussian 
   
   ➢ Spherical 
   
   ➢ Exponential 
   
   ➢ Power


Functionality for Geohashing is implemented within a framework which returns an Alphanumeric string for each latitude and longitude pair within a two dimensional grid. For performing kriging interpolation a python library called PyKrige is used.

File conversion utility contains functionalities which can convert following file formats into Feather file format.

● Parquet

● Avro

● CSV

● Excel

Feather format file is 100-150 times faster compared to CSV for reading from and writing to disk. It also takes less than half of disk space compared to CSV File. In addition, Framework has support for Feather, CSV and Excel files. These file formats can be processed within each step of the framework.

Kriging has time complexity O(N^3) and space complexity O(N^2) when there are N number of data points. To address this issue, Multithreading functionality is implemented in order to ease the task of kriging. For kriging a single file, a new thread is created.

Framework is available a[t](https://github.com/Kaatru-Senai/spatio-temporal-data-interpolation.git)[ ](https://github.com/Kaatru-Senai/spatio-temporal-data-interpolation.git)[https://github.com/Kaatru-Senai/spatio-temporal-data- ](https://github.com/Kaatru-Senai/spatio-temporal-data-interpolation.git)[interpolation.git](https://github.com/Kaatru-Senai/spatio-temporal-data-interpolation.git)[ ](https://github.com/Kaatru-Senai/spatio-temporal-data-interpolation.git)and <https://github.com/Surajbhos/Kriging_Framework>

![Alt Text] (https://github.com/Surajbhos/Kriging_Framework/blob/74657c6b1357526ca24c28a8bdaf4fe34981b84a/MathematicalF-images-0.jpg)
![Alt Text] (https://github.com/Surajbhos/Kriging_Framework/blob/74657c6b1357526ca24c28a8bdaf4fe34981b84a/MathematicalF-images-1.jpg)

**Semivariogram:**

It is the fundamental tool of Kriging. This concept explains how quickly spatial autocorrelation falls off with increasing distance.

**Features of Semivariogram:**

● Range : The distance at which semivariogram value becomes constant. Sample
 locations separated by a distance shorter than the range are uncorrelated.
 Locations farther apart than the range are uncorrelated.

● Sill : Semivariogram value at the range

● Nugget effect : Limit of semivariogram for h decreasing to zero. The nugget effect
 can be caused by measurement errors or by the fact that the process includes
 spatial variability at distances smaller than the sampling interval.

● Semivariance: A parameter that describes dissimilarity between data

![Alt Text](https://github.com/Surajbhos/Kriging_Framework/blob/09f81771c111cbeeb6cbf34387f77f5fd42c0831/Semivariogram.jpg)
Fig.1 Most common theoretical variogram models



**Validation metrics for framework:**

  To assess the performance of the framework, following validation metrics have been implemented and results are calculated with them.

**Mean Absolute Error (MAE):** The average of all absolute errors

**Root Mean Square Error (RMSE):** The standard deviation of the residuals (estimated errors)

**Mean Absolute Percentage Error (MAPE):** It measures absolute magnitude of error produced by model or how far off predictions on average

**Mean Directional Accuracy (MDA):** It compares the forecast direction (upward or downward) to the actual realized direction.

**Nash-Sutcliffe Efficiency (NSE):** It determines the relative magnitude of residual variance compared to the measured data variance

**Results:**

Alandur - Chennai

MAE MSE RMSE MDA sMAPE MAPE NSE

68\.38 7181.65 84.74 0.44 97.70 63.54 -2.17

Chakala - Mumbai

MAE MSE RMSE MDA sMAPE MAPE NSE

58\.84 4764.99 69.02 0.48 77.33 53.51 -2.85

New Malakpet - Hyderabad

MAE MSE RMSE MDA sMAPE MAPE NSE

16\.91 598.35 24.46 0.58 40.38 51.75 -0.53




