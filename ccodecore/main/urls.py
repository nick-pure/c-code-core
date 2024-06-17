from .views import *
from django.urls import path

urlpatterns = [
    path('welcome/', main_auth, name='welcome'),
    path('welcome/login/', login, name='login'),
    path('welcome/register/', register, name='register')
]
