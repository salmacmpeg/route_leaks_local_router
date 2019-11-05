#-----------------------------------------------------------------------------------#
#this is a list of all the folders for the dataset files , and their extensions
route_views="/*.bz2"
ripe="/*.gz"
parent_dir="D:/all/Masters thesis/11_9/"
folders_extentions=[]
folders_extentions.append({"num":0,"parent_dir":parent_dir,"folder":"Dodo23Feb2012from230to330/routeview-sydney","extension":route_views})
folders_extentions.append({"num":1,"parent_dir":parent_dir,"folder":"telecomMalysia12june2015from840to1040/routeviews-sydney","extension":route_views})
folders_extentions.append({"num":2,"parent_dir":parent_dir,"folder":"telecomMalysia12june2015from840to1040/routeviews-sg","extension":route_views})
folders_extentions.append({"num":3,"parent_dir":parent_dir,"folder":"verizon12Aug2014from748to752/rrc03","extension":ripe})
folders_extentions.append({"num":4,"parent_dir":parent_dir,"folder":"Amazon30june2015from5to6pm/routeviews-eqix","extension":route_views})
folders_extentions.append({"num":5,"parent_dir":parent_dir,"folder":"Amazon30june2015from5to6pm/rrc00","extension":ripe})
folders_extentions.append({"num":6,"parent_dir":parent_dir,"folder":"Google12March2015from9to915/rcc13","extension":ripe})
folders_extentions.append({"num":7,"parent_dir":parent_dir,"folder":"Moratel6Nov2012from230to3/rrc13","extension":ripe})
folders_extentions.append({"num":8,"parent_dir":parent_dir,"folder":"Nijiria12Nov2018from2130to22/rrcc13","extension":ripe})
folders_extentions.append({"num":9,"parent_dir":parent_dir,"folder":"Internexa2ovt2014from1520to1550/rrcc15","extension":ripe})
folders_extentions.append({"num":10,"parent_dir":parent_dir,"folder":"verizon12Aug2014from748to752/rrc07","extension":ripe})
folders_extentions.append({"num":11,"parent_dir":parent_dir,"folder":"volumedrive18sep2014from7to10/rrc03","extension":ripe})
folders_extentions.append({"num":12,"parent_dir":parent_dir,"folder":"china8april2010from1550to1610/rrcc13","extension":ripe})
folders_extentions.append({"num":13,"parent_dir":parent_dir,"folder":"china8april2010from1550to1610/rrcc11","extension":ripe})
folders_extentions.append({"num":14,"parent_dir":parent_dir,"folder":"Brazil21oct2017from1100to1117/rrcc15","extension":ripe})
folders_extentions.append({"num":15,"parent_dir":parent_dir,"folder":"Brazil21oct2017from1100to1117/routeviews-saopaolo1","extension":route_views})
folders_extentions.append({"num":16,"parent_dir":parent_dir,"folder":"barazil11nov2008from155to215/rrcc15","extension":ripe})

#-----------------------------------------------------------------------------------#
#this function returns a full folder name given a number in the list, if a number is out of scope , then it return empty string
def get_folder_name(f):
    if f< len(folders_extentions):
        return folders_extentions[f]["parent_dir"]+folders_extentions[f]["folder"]+folders_extentions[f]["extension"]
    else:
        print("No such folder exists!")
        return ""

def get_folder_name_without_extension(f):
    if f< len(folders_extentions):
        return folders_extentions[f]["parent_dir"]+folders_extentions[f]["folder"]
    else:
        print("No such folder exists!")
        return ""
#-----------------------------------------------------------------------------------#
#function file_names_in_folder returns a list of filenames existing in agiven folder
# gets all file names in specific folder with specific extension attached to it
#example to path is "12/prefixes/*.json"
import glob
def file_names_in_folder(path):
    file_list=glob.glob(path)
    return file_list
#-----------------------------------------------------------------------------------#
#function extractor extracts BGP update files in .gz or .bz2 formats using the
# mrtparse library and calling th (print_all.py) script
#and returns a list of all the files that is extracted
#there is also an input parameter "read_only" , if set to 0 , it will overwrite existing files , if 1 then it will not overwrite them
#take into consideration this may consume some time
import subprocess
def extracter ( file_names_gz , read_only ):
    writer_name_list=[]
    for item in file_names_gz:
        if (item.find("bz2")>0):
            #print("inside bz2")
            newitem=item.replace("bz2","txt")
        else:
            newitem=item.replace("gz","txt")
        writer_name_list.append(newitem)
    if read_only==0:
        print("read only ",read_only)
        for item1, item2 in zip(file_names_gz,writer_name_list):
            subprocess.call(["python", "print_all.py", item1,item2])
    return writer_name_list
#-----------------------------------------------------------------------------------#
#this function returns a file name for the features saving file,it doesn't create it, if a number is out of scope , then it return empty string
def get_saving_features_file_name(f):
    if f< len(folders_extentions):
        return folders_extentions[f]["parent_dir"]+folders_extentions[f]["folder"]+"/featuressssss"+str(f)+".csv"
    else:
        print("No such folder exists!")
        return ""
#this function returns a file name for the features saving file,it doesn't create it, if a number is out of scope , then it return empty string
def get_saving_features_file_name_old(f):
    if f< len(folders_extentions):
        return folders_extentions[f]["parent_dir"]+folders_extentions[f]["folder"]+"/features.csv"
    else:
        print("No such folder exists!")
        return ""
#-----------------------------------------------------------------------------------#
#this function call all the file initiation functions
def init_files(f,read_only):
    folder_name=get_folder_name(f)
    files_names=file_names_in_folder(folder_name)
    files_names=extracter(files_names,read_only)
    feature_file_name=get_saving_features_file_name(f)
    return files_names,feature_file_name

def get_all_feature_files():
    all_features=[]
    for item in folders_extentions:
        all_features.append(get_saving_features_file_name_old(item["num"]) )
    return all_features