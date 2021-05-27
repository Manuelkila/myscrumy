from django.contrib import admin
from django.urls import path, include
from idowuscrumy import views

urlpatterns= [
    path('', views.index),
    path('movegoal/<int:goal_id>/', views.move_goal, name ='move_goal'),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home, name='home'),
    ]
