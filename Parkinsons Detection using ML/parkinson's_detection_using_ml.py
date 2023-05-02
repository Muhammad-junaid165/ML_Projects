# -*- coding: utf-8 -*-
"""Parkinson's Detection using ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gAjDPUX4UjFwUOI1neTroQtHb8G8HmHM

Libraries
"""

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm

"""Data Collection and Analysis"""

#loading dataset from csv to pandas df

parkinsons_data = pd.read_csv('/content/parkinsons.csv')

#print head of dataframe

parkinsons_data.head()

#number of rows and columns in dataframe
parkinsons_data.shape

#more info about dataset
parkinsons_data.info()

# checking for missing values in each column
parkinsons_data.isnull().sum()

# getting some statistical measures about the data
parkinsons_data.describe()

# distribution of target Variable
parkinsons_data['status'].value_counts()

# grouping the data bas3ed on the target variable
parkinsons_data.groupby('status').mean()

"""Pre Processing of data"""

X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']

print(X)
print(Y)

"""Splitting the data to training data & Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_train)

"""Model Training"""

model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy score on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score of training data : ', training_data_accuracy)

# accuracy score on training data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy score of test data : ', test_data_accuracy)

"""Predictive system"""

input_data = (177.87600,192.92100,168.01300,0.00411,0.00002,0.00233,0.00241,0.00700,0.02126,0.18900,0.01154,0.01347,0.01612,0.03463,0.00586,23.21600,0.360148,0.778834,-6.149653,0.218037,2.477082,0.165827)
# changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the data
std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")

