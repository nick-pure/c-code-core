from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1>Welcome to the Competitive Code Core!<h1>')


def page_error(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def main_auth(request):
    return render(request, 'main/main_auth.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')
