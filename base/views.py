from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
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
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    #pehla GET is method, get is func
    #below pointing to Room model name in model.py

    # rooms = Room.objects.all()    #gets all rooms from db
    
    rooms = Room.objects.filter(topic__name__icontains=q)   
    # icontains ka use filter krne ke liye, ki kuch letter bhi ho to bhi filter krke select krel
    # like title mein nhi, par desc mein bhi to wo check kr lega
    # i means it is not case sensitive
    topics = Topic.objects.all()

    context = {'rooms':rooms, 'topics': topics}  # isko link kiya home.html se sidebar case
    # (upar)inme dic ki key wala var we use in html files for traversing

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

def createRoom(request):
    form = RoomForm()
    if request.method =='POST':
        #print(request.POST)   # to print our input values in form
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)   # form will be prefilled with room vaalue

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)  # this will tell what room to update
        # ab ye jisbhi room mei jake jo change krega like uska name, to wo update ho jayega

        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
   
