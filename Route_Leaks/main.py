import numpy as np
import matplotlib.pyplot as plt
import radix
from File_Manager import *
from Alarms import *
from Announcements_Manager import *
from Radix_Tree_Manager import *
from Features_Printer import *
import time
import socket
import winsound
from socket import (getaddrinfo, gaierror,
                    inet_pton, inet_ntop, AF_INET, AF_INET6, SOCK_RAW,
                    AI_NUMERICHOST,inet_ntoa)

def main():

    folder_num= int(input("Enter folder number" ))
    overwrite=int(input("Enter 0 for overwrite , 1 to read only"))
    start_time = time.time()
    file_names,feaure_file=init_files(folder_num,overwrite)
    alarm("short")
    Dict=[]
    rtree = radix.Radix()
    count=0
    for i in range (0 ,len(file_names)):
        ann,num_updates,num_withdrawls=announcement_as(file_names[i])
        if(i==0):
            announcement_saver_to_radix_tree( ann,file_names[i],rtree)
            old_peers,avgpeers=get_peers(ann)
            old_origins,avgorigins=get_origins(ann)
            old_prefixes=get_Unique_prefixes(ann)
            old_num_updates=num_updates
            old_num_withdrawls=num_withdrawls
        else:
            old_peers,old_origins,old_prefixes=Dict_Builder(Dict,ann,file_names[i-1],file_names[i],rtree,num_updates,num_withdrawls,old_peers,old_origins,old_prefixes,old_num_updates,old_num_withdrawls)
            old_num_updates=num_updates
            old_num_withdrawls=num_withdrawls
    alarm("short")
    print_Dict(Dict,feaure_file)
    printstats(Dict,get_folder_name_without_extension(folder_num))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("end")
    alarm("short")

if __name__ == '__main__':
    main()