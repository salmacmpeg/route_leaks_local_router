'''
this file handles (3,4) of the classification process  (preprocessing)
3- generate new features
4- uniform the features

'''

from File_Manager import*
import pandas
from sklearn import preprocessing


def mean_0_1(arr):
    return (arr-arr.min())/(arr.max()-arr.min())


'''def mean_around_zero(arr):
    return (arr-arr.mean()/arr.std())'''

#this function generate new features"more independent on the ventage point statistics or time"
# and normailize them around the mean from 0 to 1 it returns the new features (23 feature) and the leak type as the first column.
def preprocess(data):
    data["avg_updatesnum"]=mean_0_1(data["updates_num"])
    data["avg_withdrawls_num"]=mean_0_1(data["withdrawls_num"])
    data["avg_peers_num"]=mean_0_1(data["peers_num"])
    data["avg_origins_num"]=mean_0_1(data["origins_num"])
    data["avg_prefixes_num"]=mean_0_1(data["prefixes_num"])
    data["avg_prefixes_num"]=mean_0_1(data["prefixes_num"])
    data["avg_update_per_peer_perpeers"]=mean_0_1(data["avg_update_per_peer"]/data["peers_num"])
    data["avg_prefix_per_peer_perpeers"]=mean_0_1(data["avg_prefix_per_peer"]/data["peers_num"])
    data["avg_new_prefixes_num_per_prefixesnumber"]=mean_0_1(data["new_prefixes_num"]/data["prefixes_num"])
    data["origins_of_new_prefixes_perorigins"]=mean_0_1(data["origins_of_new_prefixes"]/data["origins_num"])
    data["origins_of_more_specific_prefixes_perorigin"]=mean_0_1(data["origins_of_more_specific_prefixes"]/data["origins_num"])
    data["new_peers_num_per_peers"]=mean_0_1(data["new_peers_num"]/data["peers_num"])
    #data["avg_update_per_origin_perorigins"]=mean_0_1(data["avg_update_per_origin"]/data["origins_num"])
    data["avg_update_per_origin_normalized"]=mean_0_1(data["avg_update_per_origin"])
    data["avg_update_per_origin_perupdates"]=mean_0_1(data["avg_update_per_origin"]/data["updates_num"])
    data["avg_prefix_per_origin_perorigins"]=mean_0_1(data["avg_prefix_per_origin"]/data["origins_num"])
    data["avg_prefix_per_origin_perprefixes"]=mean_0_1(data["avg_prefix_per_origin"]/data["prefixes_num"])
    data["more_specific_num_per_prefixes"]=mean_0_1(data["more_specific_num"]/data["prefixes_num"])
    data["peers_of_new_prefixes_per_peers"]=mean_0_1(data["peers_of_new_prefixes"]/data["peers_num"])
    data["peers_of_more_specific_prefixes_per_peers"]=mean_0_1(data["peers_of_more_specific_prefixes"]/data["peers_num"])
    data["new_origins_num_per_origins"]=mean_0_1(data["new_origins_num"]/data["origins_num"])
    data["avg_diff_updates_num"]=mean_0_1(data["diff_updates_num"]/data["updates_num"])
    data["avg_diff_withdrawls_num"]=mean_0_1(data["diff_withdrawls_num"]/data["withdrawls_num"])
    data["avg_diff_origins_num"]=mean_0_1(data["diff_origins_num"]/data["origins_num"])
    data["avg_diff_prefixes_num"]=mean_0_1(data["diff_prefixes_num"]/data["prefixes_num"])
    data["avg_diff_peers_num"]=mean_0_1(data["diff_peers_num"]/data["peers_num"])

    data2=data.iloc[:,25:51]
    target=data.iloc[:,24]
    return data2,target