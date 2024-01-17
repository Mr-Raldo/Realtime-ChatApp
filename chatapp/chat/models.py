import datetime
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value= models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)