from django.contrib import admin
from django.urls import path
from projectApp import views

urlpatterns = [
   path("", views.index, name='projectApp'),
   path("index/", views.index, name='projectApp'),
   path("result", views.result, name='result'),
   path("input", views.input, name='input'),
   path("fakenew", views.fakenew, name='fakenew'),
   path("result_new", views.result_new, name='result_new'),
   path("login1", views.login1, name='login1'),
   path("login/", views.login1, name='login'),  # 👈 added line
   path("logout_request/", views.logout_request, name='logout_request'),
   path("register/", views.register, name='register'),
   path("precautions/", views.precautions, name='precautions'),
]
