from django.contrib import admin
from django.urls import include, path

from ccodecore.messenger.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("messenger/", index),
]