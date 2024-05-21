from datetime import datetime

from django.http import HttpResponse
from .models import User, Post
from django import forms

def index(request):
    return HttpResponse("Hi, I am glad to see you here, man!")

def add_user(request, username):
    if User.objects.filter(name=username).exists():
        return HttpResponse("That username is already taken!")
    new_user = User(name=username)
    new_user.save()
    return HttpResponse("hi man!")

def get_user(request, username):
    if User.objects.filter(name=username).exists():
        return HttpResponse("This user is here")
    else:
        return HttpResponse("This user is not here")
