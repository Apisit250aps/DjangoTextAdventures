from django.contrib import admin
from django.urls import path
from . import views as api

urlpatterns = [
    path("check", api.checker, name="check_api"),
    path("check/auth", api.is_authenticated, name="check_auth"),
    
    
    path("get/character", api.getCharacter, name="getChar"),
    path("get/monster", api.getMonster, name="getMonster"),
    path("get/class/test", api.Battle),
    path("get/logs", api.getLog),
    
    
    
    
    path('post/auth/register', api.register_api, name='register'),
    path('post/auth/login', api.login_api, name='login'),
    path('post/auth/logout', api.logout_api, name='logout'),
]
