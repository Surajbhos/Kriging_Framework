import krigtype
from krigtype import *
import threads
from threads import *
import os
from os import *
import gmm
import glob
import numpy as np
import pandas as pd
import pygeohash

# Import PyKrige library
from pykrige.ok import OrdinaryKriging
import pykrige.kriging_tools as kt
import threading
import time
import pathlib
from pathlib import PurePath, Path

def krige_data(
                clusters_files: str,
                krigged_data: str,
                merged_data: str,
                variogram : str,
                ext : str,
                grid_space : float
                ):
    """
    This code implements functionality of (Kriging + Geohashing) + Concatenating files into one file
    
    Args: 
    clusters_files (str) : path of cluster files 
    krigged_data (str) : path of folder where kriged files will be stored
    merged_data (str) : path of folder where merged dataframe file will be stored
    variogram (str) : chosen variogram model
    ext (str) : file extension
    grid_space (float) : grid interval for output data
    """
    threads.intrp(clusters_files, os.path.abspath(krigged_data), variogram, ext, grid_space)
    print(pathlib.Path().absolute())
    os.chdir(os.path.dirname(os.getcwd()))
    print(pathlib.Path().absolute())
    gmm.merge_dataframes(krigged_data, os.path.abspath(merged_data), ext)
    




    



