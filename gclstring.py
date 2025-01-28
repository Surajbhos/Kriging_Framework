import ut
import os
import glob
import numpy as np
import pandas as pd
import time
import gmm
from gmm import *


project_structure = ["input_data", "clustered_data", "clusters_files", "krigged_data", "merged_data"]

def make_clusters(
                  input_data: str,
                  clustered_data: str,
                  clusters_files: str,
                  krigged_data: str,
                  merged_data: str,
                  max_clusters: int,
                  ext: str
                 ):
    """
    Creates Project Structure [input_data, clustered_data, clusters_files, krigged_data, merged_data]
    Divides large dataset into smaller chunks using Gaussian Mixture Model clustering method
    
    Args:
    input_data (str) : path of folder where input file is stored
    clustered_data (str) : path of folder where clustered file is stored after performing Gaussian Mixture Model clustering. 
                           This file contains all datapoints along with their assigned cluster
    clusters_files (str) : path of folder where each clusters csv files are stored
    krigged_data (str) : path of folder where (kriged + geohashed) files are stored 
    merged_data (str) : path of folder where merged file is stored. all kriged files are concatenated and one resultant file is created
    max_clusters (int) : Highest number of cluster. This is user defined argument where maximum how much cluster can be created is decided by user.
                        max_clusters will be same as last cluster since highest cluster is the last cluster
    ext (str) : file extension
    """
    ut.project(project_structure)
    if gmm.gaussian_mixture("input_data","clustered_data", max_clusters, ext) is False:
        print("[-] Missing input file to interpolate data")
        return
    ut.clusters("clustered_data", 0, max_clusters, "clusters_files", ext)



 
