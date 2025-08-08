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

<embed src="https://github.com/Surajbhos/Kriging_Framework/blob/1a11d603021503ced5d7fcce649e15832df6e76d/MathematicalF.pdf" type="application/pdf">

**Mathematical formulation of Kriging :**

Let the symbol denotes the observed value of the studied spatial process at the point s. The principle of prediction is based on a weighted average of neighboring
values , where the weights depend on the distance and spatial relationship between observed points.
Mathematically, the prediction at the point can be described by the equation

The weights sum to one to assure unbiasedness condition and they are found by minimizing the estimation variance.

The random variable Z(s) can be decomposed into a trend component m(x) and a residual component R(x).



Ordinary kriging assumes stationarity of the first moment of all random variables. i.e. it

assumes constant mean which is unknown. Nonstationary conditions are taken into account by restricting the domain of stationarity to a local neighborhood and moving it across the study area. Ordinary kriging is based on the assumption that the correlation between two random variables depends only on their spatial distance that separates them and is independent of their position. The variance of the difference

of two random variables and depends only on their spatial distance h.

Where, is called variogram and is a semivariogram.

The residual component is modeled as a stationary random variable with zero mean and under the assumption of intrinsic stationarity, its spatial dependence is given by the semivariance

Assuming a constant mean above equation is equivalent to:

Error in prediction i.e Kriging variance associated to an Ordinary Kriging estimate is:

**Second order stationarity and use of Universal Kriging:**

If the first moment of the observed field is not stationary and a polynomial trend occurs in the data, it is appropriate to use Universal kriging.

Universal kriging considers that is not constant, but that it varies smoothly within

the local neighborhood, representing a local trend. The trend is recalculated within each local neighborhood. This trend component is modeled as a weighted sum of

known functions and unknown coefficients ,


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




