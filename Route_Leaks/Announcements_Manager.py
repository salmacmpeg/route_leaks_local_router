
import json
#-----------------------------------------------------------------------------------#
#this function parces the MRT files and extracts the needed information from them
def announcement_as (filename):
    AS_num=" "
    AS_source=" "
    number_of_as=0
    announcement4=[]
    num_updates=0
    num_withdrawls=0
    with open(filename, 'r') as f:
        for line in f:
            if 'MRT Header' in line:
                AS_num=" "
                AS_source=" "
                number_of_as=0
                AS_List=[]
                version=" "
            elif 'Address Family:' in line:
                entries=line.strip().split(":", 2)
                version=entries[1]
            elif 'Peer AS Number:' in line:
                entries=line.strip().split(":", 2)
                AS_num=entries[1]
            elif 'Withdrawn Routes:' in line:
                entries = line.strip().split(" ", 3)
                routes=entries[2]
                if version==" 1(IPv4)":
                    announcement4.append({"peer_AS_num":AS_num ,"source_AS_num":AS_num,
                                          "case": "withdrawn",
                                          "prefix": routes,"AS_List":AS_List,"AS_Length":-1})
                    num_withdrawls+=1
            elif 'Path Segment Length: 'in line:
                entries=line.strip().split(":",2)
                number_of_as=int((entries[1].strip().split(" ",1))[0])
            elif 'Path Segment Value:' in line:
                entries=line.strip().split(" ",number_of_as+3)
                for i in range(3,(number_of_as+3)):
                    AS_List.append(entries[i])
                AS_source=entries[number_of_as+2]
            elif 'NLRI:' in line:
                entries = line.strip().split(" ", 2)
                routes=entries[1]
                if version==" 1(IPv4)":
                    announcement4.append({"peer_AS_num":AS_num,"source_AS_num":AS_source,
                                          "case": "update",
                                          "prefix": routes,"AS_List":AS_List ,"AS_Length":number_of_as})
                    num_updates+=1

    f.close()

    return announcement4,num_updates,num_withdrawls
#-----------------------------------------------------------------------------------#
def get_peers(updates_ann):
    peers=({})
    for item2 in updates_ann:
        if str(item2["peer_AS_num"]) in peers:
            peers[str(item2["peer_AS_num"]) ] +=1
        else:
            peers[str(item2["peer_AS_num"]) ]=1
    avg=0
    for i in peers:
        avg+=peers[i]
    avg=int(avg/len(peers) )
    #print("avg is ",avg)
    return(peers,avg)

def get_origins(updates_ann):
    origins=({})
    for item2 in updates_ann:
        if str(item2["source_AS_num"]) in origins:
            origins[str(item2["source_AS_num"]) ] +=1
        else:
            origins[str(item2["source_AS_num"]) ]=1
    avg=0
    for i in origins:
        avg+=origins[i]
    avg=int(avg/len(origins) )
    #print("avg is ",avg)
    return(origins,avg)

def get_Unique_prefixes(updates_ann):
    prefixes=({})
    peer_prefixes=({})
    origin_prefixes=({})
    AS_path_prefixes=({})
    for item3 in updates_ann:
        if str(item3["prefix"]) in prefixes:
            prefixes[str(item3["prefix"]) ] +=1
        else:
            prefixes[str(item3["prefix"]) ]=1
            peer_prefixes[str(item3["prefix"])]=item3["peer_AS_num"]
            origin_prefixes[str(item3["prefix"])]=item3["source_AS_num"]
            AS_path_prefixes[str(item3["prefix"])]=item3["AS_List"]
    d=[]
    for k in prefixes.keys() & peer_prefixes.keys() & origin_prefixes.keys():
        pref_entries=k.strip().split("/",2)
        pref_entries_groups=pref_entries[0].strip().split(".",4)
        d.append({"prefix":k ,"number":prefixes[k],"peer":peer_prefixes[k] ,"origin":origin_prefixes[k],"AS_List":AS_path_prefixes[k]} )
    return d

def get_Unique_prefixes_per_peer(announcement):
    #select needed keys,values pairs
    part_dict=[]
    for item in announcement:
        if item['case']=="update":
            part_dict.append({k: item[k] for k in item.keys() & {'peer_AS_num', 'prefix'}})

    #sort according to peers then prefixes
    sortedlist = sorted(part_dict , key=lambda elem: "%s %s" % (elem['peer_AS_num'], elem['prefix']))

    peer_unique_prefixes_list=[]
    peer_unique_prefixes_list.append(sortedlist[0])
    for i in range(0,len(sortedlist)-1):
        if sortedlist[i+1]!=sortedlist[i]:
            peer_unique_prefixes_list.append(sortedlist[i+1])

    peers_unique_prefixes_count,avgpeer=get_peers(peer_unique_prefixes_list)
    #print(len(peer_unique_prefixes_list))
    #print("peer_unique_prefixes_list",peer_unique_prefixes_list)
    #print("peers_unique_prefixes_count",peers_unique_prefixes_count)
    avg=0
    for i in peers_unique_prefixes_count:
        avg+=peers_unique_prefixes_count[i]
    avg=int(avg/len(peers_unique_prefixes_count) )
    #print(avg)
    return peers_unique_prefixes_count,avg

def get_Unique_prefixes_per_origin(announcement):
    #select needed keys,values pairs
    part_dict=[]
    for item in announcement:
        if item['case']=="update":
            part_dict.append({k: item[k] for k in item.keys() & {'source_AS_num', 'prefix'}})

    #sort according to peers then prefixes
    sortedlist = sorted(part_dict , key=lambda elem: "%s %s" % (elem['source_AS_num'], elem['prefix']))

    origin_unique_prefixes_list=[]
    origin_unique_prefixes_list.append(sortedlist[0])
    for i in range(0,len(sortedlist)-1):
        if sortedlist[i+1]!=sortedlist[i]:
            origin_unique_prefixes_list.append(sortedlist[i+1])

    origins_unique_prefixes_count,avgorigin=get_origins(origin_unique_prefixes_list)
    #print(len(origin_unique_prefixes_list))
    avg=0
    for i in origins_unique_prefixes_count:
        avg+=origins_unique_prefixes_count[i]
    avg=int(avg/len(origins_unique_prefixes_count) )

    return origins_unique_prefixes_count,avg

def change_in_peers_or_origins (peers1,peers2):
    peerslist1=[]
    peerslist2=[]
    for item in peers1:
        peerslist1.append(item)
    for item in peers2:
        peerslist2.append(item)
    intersection=list(set(peerslist2)-set(peerslist1))
    return intersection

import collections
import csv
def findsource(file_name2,more_specific,new_prefixes,origins_new_prefixes,peers_new_prefixes,origins_more_specific_prefixes,peers_more_specific_prefixes,AS_path_new_prefixes,AS_path_more_specific_prefixes):
    if len(more_specific)>0:
        counter1=collections.Counter(origins_more_specific_prefixes)
        #print(counter1.most_common(1))
        counter2=collections.Counter(peers_more_specific_prefixes)
        #print(counter2.most_common(1))
        counter3=collections.Counter(tuple(item) for item in AS_path_more_specific_prefixes)
        #print(counter3.most_common(1))
        file_name=file_name2.replace(".txt","more_specific.csv")
        with open(file_name, "w",newline='') as f:
            w = csv.writer(f)
            names=["origins of more specific prefixes ","count"]
            w.writerow(names)
            for item in counter1.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)
            names=["peers of more specific prefixes ","count"]
            w.writerow(names)
            for item in counter2.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)
            names=["As pathes of more specific prefixes ","count"]
            w.writerow(names)
            for item in counter3.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)

    if len(new_prefixes)>0:
        counter4=collections.Counter(origins_new_prefixes)
        #print(counter4.most_common(1))
        counter5=collections.Counter(peers_new_prefixes)
        #print(counter5.most_common(1))
        counter6=collections.Counter(tuple(item) for item in AS_path_new_prefixes)
        #print(counter6.most_common(1))
        file_name=file_name2.replace(".txt","new_prefixes.csv")
        with open(file_name, "w",newline='') as f:
            w = csv.writer(f)
            names=["origins of new prefixes ","count"]
            w.writerow(names)
            for item in counter4.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)
            names=["peers of new prefixes ","count"]
            w.writerow(names)
            for item in counter5.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)
            names=["As pathes of new prefixes ","count"]
            w.writerow(names)
            for item in counter6.most_common(10) :
                values=[]
                values.append(item[0])
                values.append(item[1])
                w.writerow(values)


    return
