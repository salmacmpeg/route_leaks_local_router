from Radix_Tree_Manager import *
from Announcements_Manager import *
import numpy as np
import csv
def print_Dict(Dict,file_name):
    with open(file_name, "w",newline='') as f:
        w = csv.writer(f)
        dickeys=[]
        for key,val in Dict[0].items():
            dickeys.append(key)
        dickeys.append("Leak_type")
        w.writerow(dickeys)
        for item in Dict:
            valarr=[]
            for key, val in item.items():
                valarr.append(val)
            valarr.append('0')
            w.writerow(valarr)
import matplotlib.pyplot as plt
def drawplt(x,y,color,xlabel,ylabel,folder):
    plt.figure(figsize=(10,5))
    plt.plot(x, y, color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.title(ylabel)
    #plt.xlim(xmin=1.0,xmax=1.0)
    plt.xticks(np.arange(0.0, max(x)+1, 1.0),rotation=0)
    extention=".png"
    plt.savefig(folder+'/'+ylabel+extention)
    #plt.show()
    plt.gcf().clear()
    plt.clf()
    plt.cla()
    plt.close()

def printstats(Dic,folder):
    timestamp=[]
    updates=[]
    withdrawals=[]
    peers=[]
    origins=[]
    prefixes=[]
    newprefixes=[]
    morespecific=[]
    xlabel="Time in Hours"
    for item in Dic:
        timestamp.append((float(item["timestamp"])/100))
        updates.append(item["updates_num"])
        withdrawals.append(item["withdrawls_num"])
        peers.append(item["peers_num"])
        origins.append(item["origins_num"])
        prefixes.append(item["prefixes_num"])
        newprefixes.append(item["new_prefixes_num"])
        morespecific.append(item["more_specific_num"])
    drawplt(timestamp,updates,"b",xlabel,"updates_num",folder)
    drawplt(timestamp,withdrawals,"b",xlabel,"withdrawals_num",folder)
    drawplt(timestamp,peers,"b",xlabel,"peers_num",folder)
    drawplt(timestamp,origins,"b",xlabel,"origins_num",folder)
    drawplt(timestamp,prefixes,"b",xlabel,"prefixes_num",folder)
    drawplt(timestamp,newprefixes,"b",xlabel,"new_prefixes_num",folder)
    drawplt(timestamp,morespecific,"b",xlabel,"more_specific_prefixes_num",folder)
    return


def Dict_Builder(Dict,updates_ann,file_name,file_name_2,rtree,num_updates,num_withdrawls,old_peers,old_origins,old_prefixes,old_num_updates,old_num_withdrawls):

    peers,avg_update_per_peer=get_peers(updates_ann)
    origins,avg_update_per_origin=get_origins(updates_ann)
    prefixes=get_Unique_prefixes(updates_ann)
    peers_unique_prefixes_count,avg_prefix_per_peer=get_Unique_prefixes_per_peer(updates_ann)
    origins_unique_prefixes_count,avg_prefix_per_origin=get_Unique_prefixes_per_origin(updates_ann)
    more_specific,new_prefixes,origins_new_prefixes,peers_new_prefixes,origins_more_specific_prefixes,peers_more_specific_prefixes,AS_path_new_prefixes,AS_path_more_specific_prefixes=update_tree_and_extract_features(updates_ann,file_name,file_name_2,rtree,prefixes)
    new_peers_num=change_in_peers_or_origins(old_peers,peers)
    new_origins_num=change_in_peers_or_origins(old_origins,origins)
    entries=file_name_2.strip().split(".", 4)
    timestamp=(entries[2])
    ''' Dict.append({ 
                  "file_name":file_name_2 ,"timestamp":timestamp,"updates_num":num_updates,"withdrawals_num":num_withdrawls
                 ,"peers_num":len(peers),"origins_num":len(origins),"prefixes_num":len(prefixes)
                 ,"new_prefixes_num":len(new_prefixes),"more_specific_num":len(more_specific)
                }) '''
    Dict.append({
        "file_name":file_name_2 ,"timestamp":timestamp,"updates_num":num_updates,"diff_updates_num":(num_updates-old_num_updates),"withdrawls_num":num_withdrawls,"diff_withdrawls_num":(num_withdrawls-old_num_withdrawls)
        ,"peers_num":len(peers),"diff_peers_num":(len(peers)-len(old_peers)),"origins_num":len(origins),"diff_origins_num":(len(origins)-len(old_origins)),"prefixes_num":len(prefixes),"diff_prefixes_num":(len(prefixes)-len(old_prefixes))
        ,"avg_update_per_peer":avg_update_per_peer,"avg_update_per_origin":avg_update_per_origin
        ,"avg_prefix_per_peer":avg_prefix_per_peer,"avg_prefix_per_origin":avg_prefix_per_origin
        ,"new_prefixes_num":len(new_prefixes),"more_specific_num":len(more_specific)
        ,"origins_of_new_prefixes":len(set(origins_new_prefixes)) ,"peers_of_new_prefixes":len(set(peers_new_prefixes))
        ,"origins_of_more_specific_prefixes":len(set(origins_more_specific_prefixes)) ,"peers_of_more_specific_prefixes":len(set(peers_more_specific_prefixes))
        ,"new_peers_num":len(new_peers_num),"new_origins_num":len(new_origins_num)
        #,"updates_change_in_peers_of_more_specific":updates_change_in_peers_of_more_specific
        #,"updates_change_in_origins_of_more_specific":updates_change_in_origins_of_more_specific
        # new origins num , new peers num , as path length things
    })
    return  peers,origins,prefixes
