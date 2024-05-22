from django.http import HttpResponse
from django.shortcuts import render
from main.models.User import User


def test_re(request, req):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<p>{req}</p>')

