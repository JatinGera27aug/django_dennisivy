#this one is for handling urls of particular apps

from django.urls import path
from . import views

#idhar ham saaman/request le rhe hain
urlpatterns=[
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room") #pointing to views of base

]
#why we have provided name var here: so that if sometime we changes our
# template name from room to smthng else, we don't have to change url
# in every folder, name=room will keep care of it
# so no need to paas url , just put name 