import os
import pandas as pd
import numpy as np
import glob


def project(project_dirs: list):
    """
    This function creates directories from list given in argument
    """
    for directory in project_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory) 



def clusters(inp_path: str, start: int, end: int, out_dir: str, ext: str, step: int=1):
    """
    This function groups all datapoints belonging to the same cluster in one csv file 
    which will be stored in clusters_files folder as a individual cluster file.

    Args:
    inp_path (str): path of folder where clustered csv file is stored
    start (int): 0 (starting clustering from 0)
    end (int): last cluster in the clustered dataset file
    out_dir (str): path of folder where individual cluster files wil be saved
    ext (str): file extension
    step (int): making clusters one by one 
    """
    if ext == "csv":
        input_file = glob.glob(f"{inp_path}/*.csv")
        if len(input_file) == 0:
            return False
        df = pd.read_csv(input_file[0])
    elif ext == "xlsx":
        input_file = glob.glob(f"{inp_path}/*.xlsx")
        print(input_file)
        if len(input_file) == 0:
            return False
        df = pd.read_excel(input_file[0])
    elif ext == "feather":
        input_file = glob.glob(f"{inp_path}/*.feather")
        print(input_file)
        if len(input_file) == 0:
            return False
        df = pd.read_feather(input_file[0])
    else:
        print('enter correct file type')
    

    for i in range(start, end, step):
        df2 = df.loc[df["Cluster"] == i]
        print(df2.shape)
        if ext == "csv":
            df2.to_csv(f"{out_dir}/Clst_{i}.csv", index=False)
        elif ext == "xlsx":
            df2.to_excel(f"{out_dir}/Clst_{i}.xlsx", index=False)
        elif ext == "feather":
            df2.reset_index().to_feather(f"{out_dir}/Clst_{i}.feather")
            






