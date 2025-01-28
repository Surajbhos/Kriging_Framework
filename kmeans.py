import pandas as pd
import numpy as np
import glob
import sklearn
from sklearn.cluster import KMeans

def create_clusters(input_csv_folder_path: str, output_csv_folder: str, cluster_size: int, ext : str):
    """
    Divides large dataset into smaller chunks using kmeans clustering.
    
    Args:
    input_csv_folder (str) : path of input file.
    output_csv_folder (str): path of folder where clustered files will reside.
    cluster_size (int) : approximate number of data points which should be present in the cluster
    ext (str) : file extension
    """

    csv_file = glob.glob(f"{input_csv_folder_path}/*.csv")
    excel_file = glob.glob(f"{input_csv_folder_path}/*.xlsx")
    feath_file = glob.glob(f"{input_csv_folder_path}/*.feather")

    
    print(csv_file)    
    print(excel_file)
    print(feath_file)

    if ext == "csv":
        if len(csv_file) == 0:
            return False
        df = pd.read_csv(csv_file[0])
        print(df)
    elif ext == "feather":
        if len(feath_file) == 0:
            return False
        df = pd.read_feather(feath_file[0])
    elif ext == "xlsx":
        if len(excel_file) == 0:
            return False
        df = pd.read_excel(excel_file[0])
    else:
        print('check file type')
    
    
    num_clusters = len(df)//cluster_size
    coordinate_array = df.loc[:, ['latitude', 'longitude', 'pm2.5']]
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++')
    kmeans.fit(coordinate_array[coordinate_array.columns[0:2]])
    coordinate_array['cluster_label'] = kmeans.fit_predict(coordinate_array[coordinate_array.columns[0:2]])
    
    
    for cluster in range(num_clusters):
            df_cluster = coordinate_array[coordinate_array['cluster_label'] == cluster]
            if ext == "csv":
                df_cluster.to_csv(f"{output_csv_folder}/Cluster_{cluster}.csv", index=False)
            elif ext == "feather":
                df_cluster.reset_index().to_feather(f"{output_csv_folder}/Cluster_{cluster}.feather")
            elif ext == "xlsx":
                df_cluster.to_excel(f"{output_csv_folder}/Cluster_{cluster}.xlsx", index=False)
            else:
                print('check file type')
    return True