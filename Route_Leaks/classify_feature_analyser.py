#make for rf and svm
from File_Manager import*
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

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
print(part1)