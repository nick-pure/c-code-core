from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('messenger/', test_menu, name='messenger'),
]
