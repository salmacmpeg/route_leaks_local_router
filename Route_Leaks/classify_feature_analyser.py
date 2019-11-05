#make for rf and svm
from File_Manager import*
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
#print(get_all_feature_files()[0])
#print(pandas.__version__)
dataset=pandas.read_csv(get_all_feature_files()[0])
'''
print(dataset.shape)
print(dataset.head(2))
print(dataset.describe())
print(dataset.groupby('Leak_type').size())
'''
#print(dataset.iloc[0:4,2:4])
'''
# box and whisker plots
dataset.iloc[:,2:6].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,6:10].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,10:14].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,14:18].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,18:22].plot(kind='box', subplots=True, layout=(4,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,22:25].plot(kind='box', subplots=True, layout=(4,2), sharex=False, sharey=False)
plt.show()

'''

part1=dataset.iloc[:,2:6]
part2=dataset.iloc[:,6:10]
part3=dataset.iloc[:,10:14]
part4=dataset.iloc[:,14:18]
part5=dataset.iloc[:,18:22]
part6=dataset.iloc[:,22:25]
'''
# histograms
part1.hist()
plt.show()

part2.hist()
plt.show()

part3.hist()
plt.show()

part4.hist()
plt.show()

part5.hist()
plt.show()

part6.hist()
plt.show()
'''
'''
scatter_matrix(part6)
plt.show()
'''
#print(part1)

# Split-out validation dataset
array = dataset.values
X = array[:,1:23]
Y = array[:,24]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

print(Y_validation)
#merge dataset
#choose features , uniform them (preprocessing)
#---------------------------------------------------------------------
# feature scaling (standard scaling by making the mean=0
#sc_X = StandardScaler()
#---------------------------------------------------------------------

#feature scaling from 0 to 1
#from sklearn.preprocessing import MinMaxScaler
# import some data
#sc = MinMaxScaler()
#data = sc.fit_transform(data))
#---------------------------------------------------------------------
#select best from skitlearn
from sklearn.feature_selection import SelectKBest
#log transform to make differences closer
#use numpy.log
#perform splitting (startified sampling)
#try to do oversampleing/undersampling techniques
#you can use imbalanced learn library
#classify
#report results
#add the two route leaks incidents in 2019

from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import NearMiss # doctest: +NORMALIZE_WHITESPACE
print('Original dataset shape %s' % Counter(dataset.iloc[:,24]))

nm = NearMiss(version=3)
X_res, y_res = nm.fit_resample(dataset.iloc[:,2:23], dataset.iloc[:,24])
print('Resampled dataset shape %s' % Counter(y_res))
