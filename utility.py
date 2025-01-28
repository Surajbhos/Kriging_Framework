import os
import glob
import pygeohash
import time
import pandas as pd
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from pykrige.ok import OrdinaryKriging

geohashing_function = np.vectorize(pygeohash.encode)
GEOHASH_PRECISION = 8

def create_directories(directory_names: list):
    """
    Creates the directories for storing un-processed and processed data
    
    Args:
    directory_names (list)  : list of names(as string) 
    """

    for directory in directory_names:
        if not os.path.exists(directory):
            os.makedirs(directory)


def csv_kriging(input_csv_files_path: str, output_csv_files_path: str, variogram : str, ext : str, grid_space: float):
    """
    Implements Ordinary Kriging method on the clustered, smaller datasets. Universal Kriging interpolates the values of desired feature
    in the grid and also gives prediction error.

    Args:
    input_csv_files_path (str) : path of folder where cluster csv files are stored
    output_csv_files_path (str) : path of folder where kriged files will be saved
    variogram (str) : chosen variogram model
    ext (str) : file extension
    grid_space (float) : grid interval for output data.
    """
   
    file_list = glob.glob(f"{input_csv_files_path}/*.csv")

    for index, file in enumerate(file_list):
        df = pd.read_csv(file)

        lons = np.array(df['longitude'])
        lats = np.array(df['latitude'])
        pm25 = np.array(df['pm2.5'])

        # Defining the grid
        longitude_grid = np.arange(np.amin(lons), np.amax(lons), grid_space)
        latitude_grid = np.arange(np.amin(lats), np.amax(lats), grid_space)
        
        # Perform Ordinary Kriging on given data
        kriging_model = OrdinaryKriging(lons, lats, pm25, variogram_model= variogram, verbose=True, enable_plotting=False,nlags=20)
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
        return_df.to_csv(f"{output_csv_files_path}/Cluster_{index}_kriged.csv", index=False)
   

def feather_kriging(input_csv_files_path: str, output_csv_files_path: str, variogram : str, ext : str, grid_space: float):
    """
    Implements Ordinary Kriging method on the clustered, smaller datasets. Universal Kriging interpolates the values of desired feature
    in the grid and also gives prediction error.

    Args:
    input_csv_files_path (str) : path of folder where clusters individual files are stored
    output_csv_files_path (str) : path of folder where kriged files will be saved
    variogram (str) : chosen variogram model
    ext (str) : file extension
    grid_space (float) : grid interval for output data.
    """
    
    file_list = glob.glob(f"{input_csv_files_path}/*.feather")

    for index, file in enumerate(file_list):
        df = pd.read_feather(file) 

        lons = np.array(df['longitude'])
        lats = np.array(df['latitude'])
        pm25 = np.array(df['pm2.5'])

        # Defining the grid
        longitude_grid = np.arange(np.amin(lons), np.amax(lons), grid_space)
        latitude_grid = np.arange(np.amin(lats), np.amax(lats), grid_space)
        
        # Perform Ordinary Kriging on given data
        kriging_model = OrdinaryKriging(lons, lats, pm25, variogram_model= variogram, verbose=True, enable_plotting=False,nlags=20)
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
        return_df.reset_index().to_feather(f"{output_csv_files_path}/Cluster_{index}_kriged.feather")

def excel_kriging(input_csv_files_path: str, output_csv_files_path: str, variogram : str, ext : str, grid_space: float):
    """
    Implements Ordinary Kriging method on the clustered, smaller datasets. Universal Kriging interpolates the values of desired feature
    and also gives prediction error.

    Args:
    input_csv_files_path (str) : path of folder where clusters individual files are stored
    output_csv_files_path (str) : path of folder where kriged files will be saved
    variogram (str) : chosen variogram model
    ext (str) : file extension
    grid_space (float) : grid interval for output data.
    """
   
    file_list = glob.glob(f"{input_csv_files_path}/*.xlsx")

    for index, file in enumerate(file_list):
        df = pd.read_excel(file)

        lons = np.array(df['longitude'])
        lats = np.array(df['latitude'])
        pm25 = np.array(df['pm2.5'])

        # Defining the grid
        longitude_grid = np.arange(np.amin(lons), np.amax(lons), grid_space)
        latitude_grid = np.arange(np.amin(lats), np.amax(lats), grid_space)
        
        # Perform Ordinary Kriging on given data
        kriging_model = OrdinaryKriging(lons, lats, pm25, variogram_model= variogram, verbose=True, enable_plotting=False,nlags=20)
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
        return_df.to_excel(f"{output_csv_files_path}/Cluster_{index}_kriged.xlsx", index=False)



# function for concatenating records in one dataframe
def merge_dataframes(input_file_path: str, output_file_path: str, ext : str, filename: str="kmeans_merged_data"):
    """
    This code is responsible for concatenating all kriged files into one merged file of desired file format
    
    Args:
    input_file_path (str): path of folder where kriged files are stored
    output_file_path (str): path of folder where merged file will be stored after concatenating all kriged files
    ext : file extension
    filename (str): name of file
    """
    if ext == "csv":
        file_list = glob.glob(f"{input_file_path}/*.csv")
        print(file_list)
        dataframes = []
        for file in file_list:
            df = pd.read_csv(file)
            dataframes.append(df)
    elif ext == "xlsx":
        file_list = glob.glob(f"{input_file_path}/*.xlsx")
        print(file_list)
        dataframes = []
        for file in file_list:
            df = pd.read_excel(file)
            dataframes.append(df)
    elif ext == "feather":
        file_list = glob.glob(f"{input_file_path}/*.feather")
        print(file_list)
        dataframes = []
        for file in file_list:
            df = pd.read_feather(file)
            dataframes.append(df)
    else:
        print('check file type')

    output = pd.concat(dataframes, axis=0, ignore_index=True)
    print(f"[+] Shape of output data: {output.shape}")

    if ext == "csv":
        output.to_csv(f"{output_file_path}/{filename}.csv", index=False)
    elif ext == "xlsx":
        output.to_excel(f"{output_file_path}/{filename}.xlsx", index=False)
    elif ext == "feather":
        output.to_feather(f"{output_file_path}/{filename}.feather")
    else:
        print('check file type')
    