from django.db import models

# Create your models here.

# here we will create our database tables
# for the users and posts

class Room(models.Model):
    #host = 
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  #2nd blan = True is for save mehtod, frist was for database null=True wla

    #null = False means db can't have instance without nothing in that attribute
    # with null=True it can be blank for desc

    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

