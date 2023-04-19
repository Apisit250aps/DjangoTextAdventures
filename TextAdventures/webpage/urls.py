from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.Menu, name='menu_page'),
    path('login', views.Login, name='login_page'),
    path('register', views.Register, name='register_page'),
    
]
