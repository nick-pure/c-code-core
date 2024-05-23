from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from main.models.User import User


def test_re(request, req):
    if int(req) == 1:
        return redirect('main', permanent=True)

    return HttpResponse(f'<p>{req}</p>')

