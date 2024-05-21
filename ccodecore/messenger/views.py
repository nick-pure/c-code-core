from django.http import HttpResponse
from django.shortcuts import render
from main.models.User import User


def index(request):
    all_users = User.objects.filter(nickname='test')

    print(all_users)

    return HttpResponse(f'<h1>Test<h1>')