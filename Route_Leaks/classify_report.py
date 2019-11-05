'''
this file handles (9) of the classification process  (preprocessing)
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
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced

#this function prints a report for the classifier
def report(y_test,y_predic):
    cm=pd.crosstab(y_test, y_predic, rownames=['Actual type'], colnames=['Predicted type'])
    print(cm)
    print(y_predic.shape)
    print(y_predic)
    print(confusion_matrix(y_test, y_predic))
    print(classification_report(y_test, y_predic))
    print(classification_report_imbalanced(y_test, y_predic))
    return