'''
this file handles (8) of the classification process  (preprocessing)
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
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import tree

def randomforestc(): #acc =87%
    #clf = RandomForestClassifier(n_jobs=5, random_state=0)
    clf = RandomForestClassifier(n_estimators=100, max_depth=2,n_jobs=5, random_state=0)
    return clf
def svmc(): #acc =88%
    clf = svm.SVC(gamma='scale')
    return clf
def decisiontreec(): #acc= 84%
    clf = tree.DecisionTreeClassifier()
    return clf
#this function classify the data and returns the predicate
def classify(x_train,y_train,xtest,choice):
    if choice==1:
        clf=randomforestc()
    elif choice==2:
        clf=svmc()
    else:
        clf=decisiontreec()
    clf.fit(x_train, y_train)
    y_predic=clf.predict(xtest)
    return y_predic