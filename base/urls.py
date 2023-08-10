#this one is for handling urls of particular apps

from django.urls import path
from . import views

#idhar ham saaman/request le rhe hain
urlpatterns=[
    path('', views.home, name="home"),
    path('room/', views.room, name="room") #pointing to views of base

]
