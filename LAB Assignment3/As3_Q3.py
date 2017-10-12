from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split


# Choose one of the dataset using the datasets features in the scikit learn
#2)Load the dataset
irisdataset=datasets.load_iris()
x = irisdataset.data
y = irisdataset.target
print(x)
print(y)
#split the data to 20% testing data, 80% training data(
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)

#linear kernel
model1 = LinearSVC(random_state=0)
#RBF kernel
model2 = svm.SVC(kernel='rbf')
model1.fit(x_train,y_train)
model2.fit(x_train,y_train)

y_prdic1 = model1.predict(x_test)
y_predic2 = model2.predict(x_test)
#predic accuracies in both cases
print("Linear Kernal Accuracy:",metrics.accuracy_score(y_test,y_prdic1))
print("RBF Kernal Accuracy",metrics.accuracy_score(y_test,y_predic2))