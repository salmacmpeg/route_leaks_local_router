import radix
from Announcements_Manager import *


def announcement_saver_to_radix_tree( updates_ann,file_name,rtree):
    print("making tree of file ", file_name)
    prefixes=get_Unique_prefixes(updates_ann)
    for dataitem in prefixes :
        rnode = rtree.add(dataitem["prefix"])
        rnode.data["Num_Updates"]=dataitem["number"]
        rnode.data["peer"]=dataitem["peer"]
        rnode.data["origin"]=dataitem["origin"]
    return rtree

def update_tree_and_extract_features(updates_ann,file_name1,file_name2,rtree,prefixes):
    more_specific=[]
    new_prefixes=[]
    origins_new_prefixes=[]
    peers_new_prefixes=[]
    origins_more_specific_prefixes=[]
    peers_more_specific_prefixes=[]
    AS_path_new_prefixes=[]
    AS_path_more_specific_prefixes=[]

    print("updating tree of file   ", file_name2)
    for dataitem in prefixes:
        prefix_len=dataitem["prefix"].strip().split("/",2)[1]
        rnode1 = rtree.search_exact(dataitem["prefix"])
        if (rnode1==None):
            new_prefixes.append(dataitem["prefix"])
            peers_new_prefixes.append(dataitem["peer"])
            origins_new_prefixes.append(dataitem["origin"])
            AS_specific_unique=[]
            [AS_specific_unique.append(item) for item in dataitem["AS_List"]  if item not in AS_specific_unique]
            AS_path_new_prefixes.append(AS_specific_unique)
            rnode2 = rtree.search_best(dataitem["prefix"])
            if (rnode2!=None):
                rnode = rtree.add(dataitem["prefix"])
                rnode.data["peer"]=dataitem["peer"]
                rnode.data["origin"]=dataitem["origin"]
                if(rnode.prefixlen> rnode2.prefixlen):
                    more_specific.append(dataitem["prefix"])
                    origins_more_specific_prefixes.append(dataitem["origin"])
                    peers_more_specific_prefixes.append(dataitem["peer"])
                    AS_specific_unique2=[]
                    [AS_specific_unique2.append(item) for item in dataitem["AS_List"]  if item not in AS_specific_unique2]
                    AS_path_more_specific_prefixes.append(AS_specific_unique2)
        else:
            rnode = rtree.add(dataitem["prefix"])
            rnode.data["peer"]=dataitem["peer"]
            rnode.data["origin"]=dataitem["origin"]

    findsource(file_name2,more_specific,new_prefixes,origins_new_prefixes,peers_new_prefixes,origins_more_specific_prefixes,peers_more_specific_prefixes,AS_path_new_prefixes,AS_path_more_specific_prefixes)

    return more_specific,new_prefixes,origins_new_prefixes,peers_new_prefixes,origins_more_specific_prefixes,peers_more_specific_prefixes,AS_path_new_prefixes,AS_path_more_specific_prefixes
