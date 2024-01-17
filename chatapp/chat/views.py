from django.shortcuts import render, redirect
from . models import Room, Message

# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request):
    return render(request,'room.html')


def checkview(request):
    room = request.POST['room-name']
    username = request.POST['username']
    # * Checking if room exists
    if Room.objects.filter(name=room).exists():
        # * Redirect to the room
        return redirect('/'+room+'/?username='+username)
