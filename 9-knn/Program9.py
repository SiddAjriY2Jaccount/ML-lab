#import
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split #Use this for Sk Learn 0.20 version
#from sklearn.cross_validation import train_test_split # Used for older versions of sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

#Input Data--->read the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv("Data_8_9.csv", names = names)
print(dataset.head())

#seperate X and Y values
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,4].values

#split the dataset ------>try various ratios here
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

#scale the training data and test data
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#change the neighbors and see the effect
#Model Creation
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(x_train, y_train)

#Prediction
y_pred = classifier.predict(x_test)
'''
for i in range(len(y_pred)):
    print ("Training Example : ")
    print(x_test[i])
    print ("Actual Label : ")
    print(y_test[i])
    print ("Predicted Label : ")
    print (y_pred[i])
    print ("--------------------------------------------")
'''
print ("Confusion Matrix : ")
print(confusion_matrix(y_test, y_pred))
print ("")
print(metrics.accuracy_score(y_test, y_pred)*100)
print ("Classification Report : ")
print(classification_report(y_test, y_pred))
