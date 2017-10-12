import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

Xdata = []
Ydata = []
X = []

#reading a csv file
def get_data(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            Xdata.append(int(row[3]))
            Ydata.append(int(row[4]))
    return
#implementing Kmean clustering on the data
def kmean_cluster(Xdata,Ydata):
    a = np.array(Xdata)
    b = np.array(Ydata)
    X = np.column_stack((a,b))
    kmeans = KMeans(n_clusters=5)
    m= kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    print(centroids)
    print(labels)
    plt.scatter(X[:, 0], X[:, 1], c=m)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()
    return

#instantiation
get_data('Customers.csv')
kmean_cluster(Xdata,Ydata)