import pandas as pd
import numpy as np
from fcmeans import FCM
import glob
import time


def fuzzy(file_path: str, clst_file_path: str, max_clusters: int, ext : str, file_name: str="cluster_files"):
    """
    This code is responsible for implementing Fuzzy C-Means algorithm on dataset and create clusters from dataset.

    Args:
    file_path (str) : path of folder where input file is stored 
    clst_file_path (str) : path of folder where clustered dataset file is stored.
    max_clusters (int) : Highest number of cluster. This is user defined argument where maximum how much clusters can be created is decided by user.
    ext (str) : file extension
    file_name (str) : Name of clustered file
    """
    if ext == "csv":
        file = glob.glob(f"{file_path}/*.csv")
        print(file)
        if len(file) == 0:
            return False
        fcm_df = pd.read_csv(file[0])   
    elif ext == "xlsx":
        file = glob.glob(f"{file_path}/*.xlsx")
        print(file)
        if len(file) == 0:
            return False
        fcm_df = pd.read_excel(file[0])   
    elif ext == "feather":
        file = glob.glob(f"{file_path}/*.feather")
        print(file)
        if len(file) == 0:
            return False
        fcm_df = pd.read_feather(file[0])
    else:
        print('check file type')
    
    
    print(fcm_df.shape)
    columns = fcm_df.columns
    data = fcm_df.values

    fcmModel = FCM(n_clusters=max_clusters)
    fcmModel.fit(data)

    center = fcmModel.centers
    pred = fcmModel.predict(data) 

    clst_df = pd.DataFrame(data, columns = columns)
    clst_df['Cluster'] = pred
    print(clst_df['Cluster'].value_counts())

    if ext == "csv":
        clst_df.to_csv(f"{clst_file_path}/{file_name}.csv", index=False)
    elif ext == "xlsx":
        clst_df.to_excel(f"{clst_file_path}/{file_name}.xlsx", index=False)
    elif ext == "feather":
        clst_df.to_feather(f"{clst_file_path}/{file_name}.feather")
    else:
        print('enter correct file type')




# function for Concatenating records into one dataframe
def merge_dataframes(input_file_path: str, output_file_path: str, ext: str, filename: str="fcm_merged_data"):
    """
    This code is responsible for concatenating all kriged files into one file
    
    Args:
    input_file_path (str): path of folder where kriged files are stored
    output_file_path (str): path of folder where merged file will be stored after concatenating all kriged files
    ext (str) : File extension
    filename (str): name of file
    """
    start_time = time.time()
    print(input_file_path)
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
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution Time is: ", elapsed_time, "seconds")
