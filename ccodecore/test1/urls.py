from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/add_user/<str:username>", views.add_user, name="add_user"),
    path("api/get_user/<str:username>", views.get_user, name="delete_user"),
]