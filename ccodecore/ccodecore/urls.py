from django.contrib import admin
from django.urls import include, path
from main.urls import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('messenger.urls'), name='messenger'),
    path("", include('main.urls'), name='main')
]

handler404 = pageError