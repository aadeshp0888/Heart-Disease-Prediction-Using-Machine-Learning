from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier


def Model_Training():
    data = pd.read_csv("C:\Users\adesh\OneDrive\Desktop\Hello\projectApp\heart_final.csv")
    data.head()

    data = data.dropna()
    
    
    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['age'] = le.fit_transform(data['age'])
    data['sex'] = le.fit_transform(data['sex'])
    data['cp'] = le.fit_transform(data['cp'])
    data['trestbps'] = le.fit_transform(data['trestbps'])
    data['chol'] = le.fit_transform(data['chol'])
    data['fbs'] = le.fit_transform(data['fbs'])
    data['restecg'] = le.fit_transform(data['restecg'])
    data['thalach'] = le.fit_transform(data['thalach'])
    data['exang'] = le.fit_transform(data['exang'])
    data['oldpeak'] = le.fit_transform(data['oldpeak'])
    data['slope'] = le.fit_transform(data['slope'])
    data['ca'] = le.fit_transform(data['ca'])
    data['thal'] = le.fit_transform(data['thal'])
  

    """Feature Selection => Manual"""
    x = data.drop(['outputlabel','target'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['outputlabel']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=10)


    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear',random_state=6)
    
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)


    
    # print("=" * 40)
    # print("==========")
    # print("Classification Report : ",(classification_report(y_test, y_pred)))
    # print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy: %.2f%%" % (accuracy * 100.0))
    # ACC = (accuracy_score(y_test, y_pred) * 100)
    # repo = (classification_report(y_test, y_pred))
    
    
    # from joblib import dump
    # dump (svcclassifier,"svmmodel_heart.joblib")
    # print("Model saved as svmmodel_heart.joblib")


    from sklearn.tree import DecisionTreeClassifier
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)


    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    from joblib import dump
    dump (svcclassifier,"DT.joblib")
    print("Model saved as DT.joblib")

def DT_Model_Training():
    data = pd.read_csv("C:/Users/LENOVO/Downloads/100%heart_disease_detection_web_updated/100%heart_disease_detection_web_updated/100%heart_disease_detection_web_updated/heart_disease_detection_web/Hello/projectApp/heart_final.csv")
    data.head()

    data = data.dropna()
    
    
    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['age'] = le.fit_transform(data['age'])
    data['sex'] = le.fit_transform(data['sex'])
    data['cp'] = le.fit_transform(data['cp'])
    data['trestbps'] = le.fit_transform(data['trestbps'])
    data['chol'] = le.fit_transform(data['chol'])
    data['fbs'] = le.fit_transform(data['fbs'])
    data['restecg'] = le.fit_transform(data['restecg'])
    data['thalach'] = le.fit_transform(data['thalach'])
    data['exang'] = le.fit_transform(data['exang'])
    data['oldpeak'] = le.fit_transform(data['oldpeak'])
    data['slope'] = le.fit_transform(data['slope'])
    data['ca'] = le.fit_transform(data['ca'])
    data['thal'] = le.fit_transform(data['thal'])
   


    """Feature Selection => Manual"""
    x = data.drop(['outputlabel','target'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['outputlabel']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=10)


    from sklearn.tree import DecisionTreeClassifier
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)


    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    from joblib import dump
    dump (svcclassifier,"DT.joblib")
    print("Model saved as DT.joblib")


Model_Training()
