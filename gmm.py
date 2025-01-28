import numpy as np
import pandas as pd
import glob
import time


def gaussian_mixture(input_file: str, clst_file: str, max_clusters: int, ext: str, file_name: str="cluster_files"):
    """
    This code is responsible for implementing gaussian mixture model clustering algorithm on dataset and create clusters from dataset.

    Args:
    input_file (str) : path of folder where input file is stored 
    clst_file (str) : path of folder where clustered dataset file is stored.
    max_clusters (int) : Highest number of cluster. This is user defined argument where maximum how much clusters can be created is decided by user.
    ext (str) : file extension
    file_name (str) : Name of clustered file
    """
    if ext == "csv":
        file = glob.glob(f"{input_file}/*.csv")
        print(file)
        if len(file) == 0:
            return False
        gmm_df = pd.read_csv(file[0])   
    elif ext == "xlsx":
        file = glob.glob(f"{input_file}/*.xlsx")
        print(file)
        if len(file) == 0:
            return False
        gmm_df = pd.read_excel(file[0])   
    elif ext == "feather":
        file = glob.glob(f"{input_file}/*.feather")
        print(file)
        if len(file) == 0:
            return False
        gmm_df = pd.read_feather(file[0])
    else:
        print('check file type')
    
    
    print(gmm_df.shape)
    print(gmm_df.head())
    
    # Getting X values from the data
    x = gmm_df.iloc[:, [0,1,2]].values

    from sklearn.mixture import GaussianMixture as GMM
    n_components = np.arange(1, 50)

    models = [GMM(n, covariance_type='full', random_state=0) for n in n_components]

    gmm = GMM(n_components= max_clusters, covariance_type='full', random_state=0).fit(x)

    labels = gmm.predict(x)

    probs = np.argmax(gmm.predict_proba(x), axis=1)

    print(probs)

    gmm_df["Cluster"] = probs
    print(gmm_df['Cluster'].value_counts())
    
    if ext == "csv":
        gmm_df.to_csv(f"{clst_file}/{file_name}.csv", index=False)
    elif ext == "xlsx":
        gmm_df.to_excel(f"{clst_file}/{file_name}.xlsx", index=False)
    elif ext == "feather":
        gmm_df.to_feather(f"{clst_file}/{file_name}.feather")
    else:
        print('enter correct file type')





# function for Concatenating records into one dataframe
def merge_dataframes(input_file_path: str, output_file_path: str, ext: str, filename: str="gmm_merged_data"):
    """
    This code is responsible for concatenating all kriged files into one file of desired file format
    
    Args:
    input_file_path (str) : path of folder where kriged files are stored
    output_file_path (str) : path of folder where merged file will be stored after concatenating all kriged files
    ext (str) : file extension
    filename (str) : name of file
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