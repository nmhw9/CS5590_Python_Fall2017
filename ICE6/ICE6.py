from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

#Load the dataset from iris
irisdataset=datasets.load_iris()
independent = irisdataset.data
dependent = irisdataset.target
print(" Data Loaded from IRIS")
print("Independent:",independent)
print("Dependent:",dependent)

#split the data to 20% testing data, 80% training data(
independent_train,independent_test,dependent_train,dependent_test=train_test_split(independent,dependent,test_size=.2)
print("Split Training and Test Sets")
print()
print("TriningData:")
print("IndependentTrain:",independent_train)
print("DependentTrain:",dependent_train)
print()
print("TestData:")
print("IndependentTrain:",independent_test)
print("DependentTrain:",dependent_test)
print()

#linear kernel
model1 = LinearSVC(random_state=0)
model1.fit(independent_train,dependent_train)
print("Given Test Data is fit using SVM model")
print()

dependent_prdic = model1.predict(independent_test)

#prediction of accuracy
print("Accuracy of SVM model fit on the Data:",metrics.accuracy_score(dependent_test,dependent_prdic))

