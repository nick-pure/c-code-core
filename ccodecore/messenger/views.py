from django.http import HttpResponse
from django.shortcuts import render

from ccodecore.main.models.User import User


def index(request):
    all_users = User.objects.all()

    print(all_users)

    return HttpResponse(f'<h1>Test<h1>')