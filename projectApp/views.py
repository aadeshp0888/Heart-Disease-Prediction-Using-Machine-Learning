from django.db import IntegrityError

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
#from projectApp.models import Register

import os
import time
import random

import requests

import requests
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
import numpy as np
import joblib
from django.contrib.auth.models import User
import pandas as pd, numpy as np, re
import os
from sklearn.metrics import classification_report, accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split
import tkinter as tk
from sklearn import svm
from PIL import Image, ImageTk
from tkinter import ttk
from joblib import dump , load
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import pickle
import nltk
import matplotlib.pyplot as plt
from django.core.mail import send_mail


#######################################################################################################
nltk.download('stopwords')
stop = stopwords.words('english')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#######################################################################################################

# Create your views here.
def index(request):
        return render(request, 'index.html')
        
def input(request):
    return render(request, 'input.html')

        
def fakenew(request):
    return render(request, 'fakenew.html')

def precautions(request):
       return render(request,'precautions.html')


def result(request):
        #if request.POST.get('action') == 'post':
            lis = []       
            # Receive data from client
            lis.append(request.GET['Age'])
            lis.append(request.GET['Gender'])
            lis.append(request.GET['Chest_Pain'])
            lis.append(request.GET['Restbp'])
            lis.append(request.GET['Chol'])
            lis.append(request.GET['FBS'])
            lis.append(request.GET['Restecg'])
            lis.append(request.GET['thalach'])
            lis.append(request.GET['Exang'])
            lis.append(request.GET['Oldpeak'])
            lis.append(request.GET['slope'])
            lis.append(request.GET['ca'])
            lis.append(request.GET['thal'])
            print(lis) 


            # Traning model
            from joblib import dump , load
            model=load('projectApp\HEART_DISEASE_MODEL.joblib')
            
            # Make prediction
            result = model.predict([lis])

            if result[0] == 0:
              print("Heart Disease")
              value = (
                '--------------- Heart Disease -------------\n\n'
                    'Dr.Khurana 9090909090, Akurdi, Pune\n'
                    'Dr. Patil 9898989898, Chinchwad, Pune'
                         )

    # Send Email
              send_mail(
              subject='Heart Disease Prediction Result',
              message=f'Your prediction result shows a high risk of heart disease.\n\nRecommendations:\n{value}',
              from_email='heartdisease.sct@gmail.com',
              recipient_list=['riyabhole19@gmail.com'],  # 🔁 Replace with user's email dynamically if available
              fail_silently=False,
                 )

            else:
                print("Normal Heart")
                value = 'Normal Heart'

            #label4 = tk.Label(root,text ="Normal Speech",width=20,height=2,bg='#FF3C3C',fg='black',font=("Tempus Sanc ITC",25))
            #label4.place(x=450,y=550)
    
            return render(request,'result.html',  {
                      'ans': value,
                      'title': 'Predict Heart Disease ',
                      'active': 'btn btn-success peach-gradient text-white',
                      'result': True,
                      
                  })
    

def result_new(request):
        #if request.POST.get('action') == 'post':
            # Traning model
            from joblib import dump , load
            model=load('DT.joblib')  
            # Receive data from client
            lis = []       
            # Receive data from client
            lis.append(request.GET['Age'])
            lis.append(request.GET['Gender'])
            lis.append(request.GET['Chest_Pain'])
            lis.append(request.GET['Restbp'])
            lis.append(request.GET['Chol'])
            lis.append(request.GET['FBS'])
            lis.append(request.GET['Restecg'])
            lis.append(request.GET['thalach'])
            lis.append(request.GET['Exang'])
            lis.append(request.GET['Oldpeak'])
            lis.append(request.GET['slope'])
            lis.append(request.GET['ca'])
            lis.append(request.GET['thal'])
            print(lis) 
            # Make prediction
            result = model.predict([lis])
            pred = np.round(result)  
            if (pred < 51):
                print("Good")
                value = 'Good'
            elif ((pred > 51) & (pred < 76)):
                print("Medium")
                value = 'Medium'
            else:
                print("Bad")
                value = 'Bad'

            price = "Heart Healthy Predict: "+str(pred[0])+ "%" + "\n" + str(value)
	    
	        
    
            return render(request,'result_new.html',  {
                      'ans': price,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'result': True,
                      
                  })

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login1')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})



def login1(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('input')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login1')