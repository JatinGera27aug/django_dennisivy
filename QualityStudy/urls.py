from django.contrib import admin
from django.urls import path, include
#from django.http import HttpResponse


#core url handler/storer


#-----pehle idhar likha but for specific app we can make seperate 
# view file in that apps' folder only-----------

# def home(reuqest): #request gonna be http
#     return HttpResponse('HOME PAGE')   # if written return only, then NONE MESSAGE ERROR
#     #yha pe waise hame link deni hongi pages ki
#     #abhi upar to bas template se return krwa rhe hain


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))  #now both files are connected
]

