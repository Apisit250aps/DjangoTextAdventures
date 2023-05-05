from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('gate', views.Gate, name='gate_page'),
    path('login', views.Login, name='login_page'),
    path('register', views.Register, name='register_page'),
    path('menu', views.Menu, name='menu_page'),
    path('character', views.Character, name='character_page'),
    
]
