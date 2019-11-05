'''
this file handles (5) of the classification process  (preprocessing)
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
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2,f_classif

#this function applys the feature selection using the chi square method with no less value than 5 , we also removed some correlated features
# the function returns the new train dataset with the selected 10 features only.
def select(data,target):
    bestfeatures = SelectKBest(score_func=chi2, k=10)
    fit = bestfeatures.fit(data,target)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(data.columns)
    #concat two dataframes for better visualization
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    featureScores.columns = ['Specs','Score']  #naming the dataframe columns
    #print(featureScores.nlargest(10,'Score'))  #print 10 best features
    newdata=pd.DataFrame(bestfeatures.transform(data))
    #print(newdata.shape)
    #print(bestfeatures.get_support(indices=True))
    newdata.columns=data.columns[bestfeatures.get_support(indices=True)]
    #print(newdata.columns)
    return newdata
'''
    from sklearn.ensemble import ExtraTreesClassifier
    import matplotlib.pyplot as plt
    model = ExtraTreesClassifier()
    model.fit(data,target)
    print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=data.columns)
    feat_importances.nlargest(12).plot(kind='barh')
    plt.show()

    import seaborn as sns
#get correlations of each features in dataset
    all=data
    all["Leak_type"]=target
    corrmat = all.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(20,20))
#plot heat map
    g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
    plt.show()
    '''
