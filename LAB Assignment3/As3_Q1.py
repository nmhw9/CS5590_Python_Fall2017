import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#varibles to fit
independent = []
dependent = []

#reading data from csv file
def get_data(filename):
    with open (filename,"r") as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dependent.append(float(row[0]))
            independent.append(float(row[4
                                     ]))
    return

#fitting the independent and dependent variables
def show_plot(independent,dependent):
    linear_mod= linear_model.LinearRegression()
    dependent = np.reshape(dependent,(len(dependent),1))
    independent=np.reshape(independent,(len(independent),1))
    linear_mod.fit( independent, dependent)
    plt.scatter(independent,dependent,color='yellow')
    plt.plot(independent,linear_mod.predict(independent),color='blue',linewidth=3)
    plt.xlabel("Weight of the Car")
    plt.ylabel("Miles per Gallon(mpg)")
    plt.show()
    return

#predict
def predict_dependent(independent,dependent,x):
    linear_mod = linear_model.LinearRegression()
    independent = np.reshape(independent,(len(independent),1))
    dependent = np.reshape(dependent,(len(dependent),1))
    linear_mod.fit(independent,dependent)
    predicted_dependent = linear_mod.predict(x)
    print("Predicted mpg for car weight",x ,"is ",predicted_dependent[0][0])
    print("Coefficient for fit is ",linear_mod.coef_[0][0])
    print("Intercept of the fit",linear_mod.intercept_[0])
    return predicted_dependent[0][0], linear_mod.coef_[0][0],linear_mod.intercept_[0]

#instantiation
get_data('Auto-rev.csv')
print("Miles per Gallon data")
print(independent)
print("Weight of the Car")
print(dependent)
show_plot(independent,dependent)
predict_dependent(independent,dependent,3000)
