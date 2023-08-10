from django.shortcuts import render

# Create your views here.

#there are gonna be what we need to render, contains whole data when someone 
# goes to particular url
#contains function here to be called on request



def home(request): 
    return render(request, 'home.html')
    #return HttpResponse('HOME PAGE') 


def room(request):
    return render(request, 'room.html')
   
