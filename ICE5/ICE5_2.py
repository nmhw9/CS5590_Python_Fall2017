
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

Xdata = []
Ydata = []
X = []

# df = pd.read_csv('ex2data1.txt', names=['exam1','exam2','admission'])
# print ("df.head",df.head())

data = pd.read_csv('Tshirt',names =['name','height',"weight"])
print(data.head())
x = np.array(data['height'],float)
y = np.array(data['weight'],float)
train_X = np.column_stack((x,y))
print(train_X)
print("Sizes Clustere are XS, S, M, L, XL")
kmeans = KMeans(n_clusters=5)
m= kmeans.fit_predict(train_X)
plt.scatter(train_X[:,0],train_X[:,1], c=m)
plt.show()

#
# #instantiation
# get_data('Customers.csv')
# kmean_cluster(Xdata,Ydata)
