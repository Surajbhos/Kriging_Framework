import ut
import krigtype
import cent
import intp
from intp import *
from krigtype import *
import threads
import os
import main
import utility
import glob
import numpy as np
import pandas as pd
import pygeohash
import gclstring
import gmmintp

# Import PyKrige library
from pykrige.ok import OrdinaryKriging
import pykrige.kriging_tools as kt
import threading
import time
from pathlib import Path


project_structure = ["input_data", "clustered_data", "clusters_files", "krigged_data", "merged_data"]

def choose_method(clustering_method: str, max_clusters: int, ext : str, grid_space:float, variogram : str):
    """
    For the choosen clustering methods, first the project structure is created. After that clusters are made from given dataset using specified
    clustering method. On these cluster files Ordinary Kriging is performed along with Geohashing. For every data point within grid kriged value,
    prediction error and geohash string are generated.


    Args: 
    clustering method (str): Clustering method is chosen from three clustering methods implemented. 
                             Available Clustering methods are Fuzzy C-Means Clustering, K-Means Clustering and Gaussian Mixture Model Clustering
    
    max_clusters (int): This is user defined argument. It denotes maximum how much clusters should be created from dataset.
    
    grid_space (float): grid interval for output data
    
    variogram (str) : chosen variogram model
    """
    if clustering_method == "fcm":
        cent.make_clusters("input_data", "clustered_data", "clusters_files", "krigged_data", "merged_data", max_clusters, ext)
        intp.krige_data("clusters_files", "krigged_data", "merged_data", grid_space, variogram, ext)
    elif clustering_method == "kmeans":
        main.interpolate_data("input_data", "clustered_data", "krigged_data", "merged_data", max_clusters, grid_space, variogram, ext)
    elif clustering_method == "gmm":
        gclstring.make_clusters("input_data", "clustered_data", "clusters_files", "krigged_data", "merged_data", max_clusters, ext)
        gmmintp.krige_data("clusters_files", "krigged_data", "merged_data", grid_space, variogram, ext)
    else:
        print('Enter correct method')



choose_method('fcm', 80, 'feather', 0.01, 'spherical')


