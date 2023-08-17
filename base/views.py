from django.shortcuts import render
from .models import Room
# Create your views here.

#there are gonna be what we need to render, contains whole data when someone 
# goes to particular url
#contains function here to be called on request



# rooms=[
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Design'},
#     {'id':3, 'name':'DSA'}
# ]

def home(request): 
    #below pointing to Room model name in model.py
    rooms = Room.objects.all()    #gets all rooms from db
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)  #2nd rooms means what value we pass

    #return HttpResponse('HOME PAGE') 


def room(request, pk):

    room = Room.objects.get(id=pk)   #now they will show room along with correct links
    #id in models are by default specified , starting from 1
    #and incrementing by one
    
    # room = None
    # for i in rooms:
    #     if i['id']==int(pk):
    #         room = i
    context = {'room':room}
    return render(request, 'base/room.html',context)
   
