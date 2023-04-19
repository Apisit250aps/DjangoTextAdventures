from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('menu', admin.site.urls),
]
