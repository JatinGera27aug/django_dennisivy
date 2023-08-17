from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

# here we will create our database tables
# for the users and posts


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # (<topicname> when it is already made or upper in code
    # else "topicname" to access anywhere)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  #2nd blan = True is for save mehtod, frist was for database null=True wla

    #null = False means db can't have instance without nothing in that attribute
    # with null=True it can be blank for desc

    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)   #inital time stamp hi store rhegi


    class Meta:
        ordering = ['-updated', '-created']  # newest room will be last
        # but opp when -updated
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade means delete fully
    # below command is used when a Room is deleted, its children will also be deleetd
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #set_null will used to remain the existence of var
    # on delete we do with one-to-many relations
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)   #inital time stamp hi store rhegi

    def __str__(self):
        return self.body[0:50]  #will return only first 50 letters
    




# for first running python manage.py makemigrations, we get 0001_initial.py in migrations older
# it will keep on increasing