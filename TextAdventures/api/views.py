from django.shortcuts import render
import json
import pytz
from PIL import Image
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login
from django.db.models import Q

from .models import *

# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def checker(request):
    status = False
    type = request.data['type']
    check = request.data['check']

    if type == 'username':
        if User.objects.filter(username=check):
            status = True
        else:
            status = False

    elif type == 'email':
        if User.objects.filter(email=check):
            status = True
        else:
            status = False

    elif type == 'knight':
        if Character.objects.filter(name=check):
            status = True
        else:
            status = False
    else:
        status = True
        type = "Error"

    print(status)

    return Response({"status": status, "type": type})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register_api(request):
    status = False
    name_req = request.data['name']
    username_req = request.data['username']
    email_req = request.data['email']
    password_req = request.data['password']

    # for i, o in request.data.items():
    #     print(i, o)

    user_create = User.objects.create_user(
        username=username_req, email=email_req, password=password_req)

    if user_create:
        print("user success!")
        char_create = Character.objects.create(
            user=user_create, name=name_req)
        if char_create:
            print("char success!")
            try:
                Inventory.objects.create(
                    character=char_create, items_id=0)
                StatusPoints.objects.create(
                    character=char_create)
                print("success!")
                status = True
            except:
                print("fail")
                User.objects.filter(username=username_req).delete()
                print("delete user")
        else:
            print("create character fails")
    else:
        print("create user fails")

    print(status)

    return Response({"status": status})


@csrf_exempt
@api_view(["POST",])
@permission_classes((AllowAny,))
def login_api(request):

    status = False

    users = request.data["username"]
    username = users
    remember = request.data["remember"]

    login_form = {
        "username": username,
        "password": request.data["password"]
    }

    user = authenticate(**login_form)

    if user is not None:
        if user.is_active:
            status = True
            msg = 'ผู้ใช้กำลังใช้งานอยู่'
            login(request, user)
        else:
            status = False
            msg = 'มีบางอย่างผิดพลาด'
    else:
        status = False
        msg = 'รหัสผ่านไม่ถูกต้อง'

    return Response({'status': status, "message": msg})
