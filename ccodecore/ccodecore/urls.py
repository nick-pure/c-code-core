from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('messenger.urls')),
    path('', include('main.urls'))
]