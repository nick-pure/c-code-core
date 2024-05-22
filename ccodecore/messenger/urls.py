from .views import *
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<req>[0-9]{1})/', test_re),
]


