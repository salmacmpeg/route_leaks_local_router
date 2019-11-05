'''
this file handles (10,call_all) of the classification process  (preprocessing)
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
from classify_read_data import *
from classify_preprocessing import *
from classify_feature_selection import *
from  classify_splitting import *
from  classify_sampling import *
from  classify_classifier import *
from  classify_report import *
#np.random.seed(0) #uncomment this to save the state
data_all= read_data()
processed_data,target =preprocess(data_all)
selected_data=select(processed_data,target)
xtrain,xtest,ytrain,ytest=split(selected_data,target)
sampled_x_train,sampled_y_train=sample(xtrain,ytrain)
ypredicted=classify(sampled_x_train,sampled_y_train,xtest)
report(ytest,ypredicted)