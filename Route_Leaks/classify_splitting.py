'''
this file handles (6) of the classification process  (preprocessing)
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
from sklearn.model_selection import train_test_split
# this function splits the data into test"20%" and train "80%" with keeping the both balanced

def split(data,target):
    X_train, X_test, y_train, y_test = train_test_split(data, target,stratify=target, test_size=0.20)
    return X_train, X_test, y_train, y_test
