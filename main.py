import utility
import time
import kmeans
import pathlib
from pathlib import Path
import os
from os import *

project_structure = ["input_data", "clustered_data", "krigged_data", "merged_data"]

def interpolate_data(
                    input_data: str,
                    clustered_data: str,
                    krigged_data: str,
                    merged_data: str,
                    cluster_size: int,
                    variogram : str,
                    ext : str,
                    grid_space:float
                    ):
    """
    This function first creates project structure from the given list.
    It checks if the input file is there in input_data directory. If it is not there then it throws error.
    If file exists then using K-Means clustering method it creates cluster files from input file.
    Ordinary Kriging applied on these files and created kriged files are stored into kriged_data folder.
    At last all the kriged files are concatenated into one file and saved to merged_data folder.
    """
    utility.create_directories(project_structure)
    if kmeans.create_clusters(input_data, clustered_data, cluster_size, ext) is False:
        print("[-] Missing input file to interpolate data")
        return
    if ext == "csv":
        utility.csv_kriging(clustered_data, os.path.abspath(krigged_data), variogram, ext, grid_space)
        utility.merge_dataframes(krigged_data, merged_data, ext)
    elif ext == "feather":
        utility.feather_kriging(clustered_data, os.path.abspath(krigged_data), variogram, ext, grid_space)
        utility.merge_dataframes(krigged_data, merged_data, ext)
    elif ext == "xlsx":
        utility.excel_kriging(clustered_data, os.path.abspath(krigged_data), variogram, ext, grid_space)
        utility.merge_dataframes(krigged_data, merged_data, ext)
    else:
        print('check file type')

    