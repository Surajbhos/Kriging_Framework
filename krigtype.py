import pandas as pd
import numpy as np
import glob
import time
import os
import pygeohash
import pathlib
import pyarrow


# Import PyKrige library
from pykrige.ok import OrdinaryKriging 

geohashing_function = np.vectorize(pygeohash.encode)
GEOHASH_PRECISION = 8


def apply_kriging(datafile: str, input_csv_files_path: str, output_csv_files_path: str, variogram : str, kriged_data_file: str, grid_space: float):
    """
    Implements Ordinary Kriging method on the clustered, smaller datasets. Ordinary Kriging interpolates the values of desired feature
    in the grid and also gives prediction error for every datapoint within grid. geohash string for each (lat,long) pair is also generated.

    Args:
    datafile (str) : file over which kriging and geohashing has to be performed
    input_csv_files_path (str) : file path of cluster files.
    output_csv_files_path (str) : file path where output kriged file will be saved
    kriged_data_file (str) : resulting kriged and geohashed file
    variogram (str) : chosen variogram model
    grid_space (float) : grid interval for output data.
    """
    
    extension = pathlib.Path(datafile).suffix
    print(extension)
    if extension == ".csv":
        df = pd.read_csv(datafile)
    elif extension == ".xlsx":
        df = pd.read_excel(datafile)
    elif extension == ".feather":
        df = pd.read_feather(datafile)
    else:
        print('check file type')

        
    lons = np.array(df['longitude'])
    lats = np.array(df['latitude'])
    pm25 = np.array(df['pm2.5'])

    # Defining the grid
    longitude_grid = np.arange(np.amin(lons), np.amax(lons), grid_space)
    latitude_grid = np.arange(np.amin(lats), np.amax(lats), grid_space)
        
    # Perform Universal Kriging with variogram model and drift on given data
    kriging_model = OrdinaryKriging(lons, lats, pm25, variogram_model=variogram, verbose=True, enable_plotting=False,nlags=19)
    interpolated_data, err = kriging_model.execute('grid', longitude_grid, latitude_grid)

    xintrp, yintrp = np.meshgrid(longitude_grid, latitude_grid)
    x_comp = np.array(xintrp)
    y_comp = np.array(yintrp)

    return_df = pd.DataFrame(columns=["latitude", "longitude", "pm2.5", "geohash", "Prediction Error"])
    return_df["longitude"] = x_comp.flatten()
    return_df["latitude"] = y_comp.flatten()
    return_df["pm2.5"] = interpolated_data.flatten()
    return_df["geohash"] = geohashing_function(return_df["latitude"], return_df["longitude"], precision=GEOHASH_PRECISION)
    return_df["Prediction Error"] = err.flatten()
    if extension == ".csv":
        return_df.to_csv(f"{output_csv_files_path}/{kriged_data_file}", index=False)  
    elif extension == ".xlsx":
        return_df.to_excel(f"{output_csv_files_path}/{kriged_data_file}", index=False)
    elif extension == ".feather":
        return_df.to_feather(f"{output_csv_files_path}/{kriged_data_file}") 
    else:
        print('check file type')    
    
    

