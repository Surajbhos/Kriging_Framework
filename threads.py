import krigtype
from krigtype import *
import os
import glob
import numpy as np
import pandas as pd

# Import PyKrige library
from pykrige.ok import OrdinaryKriging
import pykrige.kriging_tools as kt
import threading
import time



def intrp(route: str, dir: str, variogram : str, ext : str, grid_space: float):
    """
    This code is responsible for implementing Multithreading functionality for kriging.

    Args:
    route (str) : path of folder containing cluster files
    dir (str) : path of folder where kriged files will be stored
    variogram (str) : chosen variogram model
    ext (str) : file extension
    grid_space (float) : grid interval for output data

    Threading module creates new thread for each cluster file. Within thread it imports function apply_kriging from krigtype.py file
    and performs (kriging+geohashing) on that cluster file. After that, kriged file is saved to directory given in argument dir. All this process
    is done within every thread.
    
    """
    
    os.chdir(route)
    
    start_time = time.time()
    
    csv_files = glob.glob('*.{}'.format('csv'))
    
    xlsx_files = glob.glob('*.{}'.format('xlsx'))

    feather_files = glob.glob('*.{}'.format('feather'))

    print(csv_files)
    print(xlsx_files)
    print(feather_files)
    print('*****************************************************************')
    
    for i in csv_files:
        t1 = threading.Thread(target=krigtype.apply_kriging, args=(i,route,dir, variogram, f"{i}_kriged_data.csv", grid_space))
        t1.start()
        t1.join()

    for i in feather_files:   
        t2 = threading.Thread(target=krigtype.apply_kriging, args=(i,route, dir, variogram, f"{i}_kriged_data.feather", grid_space))
        t2.start()
        t2.join()


    for i in xlsx_files:
        t3 = threading.Thread(target=krigtype.apply_kriging, args=(i,route,dir, variogram, f"{i}_kriged_data.xlsx", grid_space))
        t3.start()
        t3.join()
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time :", elapsed_time, "seconds")

