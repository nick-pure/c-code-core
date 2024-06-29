from django import forms
from main.models import *


class RegisterUser(forms.Form):
    nickname = forms.CharField(max_length=12)
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=15)

    password = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=255)