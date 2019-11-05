'''
this file handles (1,2) of the classification process  (preprocessing)
1- read all data
2- integrate them to one dataframe

'''
from File_Manager import*
import pandas
def read_data():
    list=[]
    all_files=get_all_feature_files()
    for item in all_files:
        dataset=pandas.read_csv(item)
        list.append(dataset)
    data_all=pandas.concat(list,axis=0, ignore_index=True)
    data_all.to_csv(r'D:\all\Masters-Phase2\all_raw_features.csv')
    return data_all

