'''
this file handles (7) of the classification process  (preprocessing)
1- read all data
2- integrate them to one dataframe
3- generate new features
4- uniform the features
5- apply feature selection models
////// further steps
6- apply splitting to train and test
7- apply sampling techniques
8- apply classifier
9- report results
////// more further steps
10- time analysis
'''
from imblearn.over_sampling import KMeansSMOTE
import pandas as pd
# this function works on the train data to increase it's size using balancing techniques to merely the double size
def sample(xtrain,ytrain):
    sm = KMeansSMOTE(random_state=42)
    x_res, y_res = sm.fit_resample(xtrain, ytrain)
    y=y_res
    x_res=pd.DataFrame(x_res)
    #y_res=pd.DataFrame(y_res)
    x_res.columns=xtrain.columns
    #y_res.columns=["Leak_type"]
    return x_res,y_res
