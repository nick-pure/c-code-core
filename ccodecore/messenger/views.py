from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from main.models.User import User


menu = ["Create a chat", "Find friends", "Build a house"]

def test_menu(request):
    return render(
        request,
        'messenger/messenger_main.html',
        {
            'title': 'Messenger',
            'menu': menu,
        },
    )


def users_online(request):
    online_users = User.objects.filter(is_active=True)
    return render(
        request,
        'messenger/online_users.html',
        {
            'online': online_users,
        },
    )
