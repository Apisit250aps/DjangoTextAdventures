from django.contrib import admin
from django.urls import path
from . import views as api

urlpatterns = [
    path("check", api.checker, name="check_api"),
    path('register', api.register_api, name='register'),
    path('login', api.login_api, name='login'),
]
