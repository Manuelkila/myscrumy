from django.contrib import admin
from django.urls import path, include
from idowuscrumy import views

urlpatterns= [
    path('', views.index)
    ]
