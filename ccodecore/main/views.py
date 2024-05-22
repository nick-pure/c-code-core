from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1>Welcome to the Competitive Code Core!<h1>')


def pageError(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')