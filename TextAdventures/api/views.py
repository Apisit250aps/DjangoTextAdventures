
from django.shortcuts import render, redirect
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
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


from .TextAdventure import CharacterInformation, MonsterTarget, ArenaBattle
from .models import *
from . import serializers


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def is_authenticated(request):
    is_authenticate = False
    try:
        is_authenticate = '_auth_user_id' in request.session

    except:
        is_authenticate = False

    return Response({"status": is_authenticate})

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
        if Character.objects.filter(character_name=check):
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

    user_create = User.objects.create_user(
        username=username_req, email=email_req, password=password_req)

    if user_create:
        print("user success!")
        char_create = Character.objects.create(
            user=user_create,
            character_name=name_req)
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


def logout_api(request):
    logout(request)
    return redirect('gate_page')


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def getCharacter(request):

    try:
        user = User.objects.get(id=request.session['_auth_user_id'])
        character = Character.objects.get(user=user)
        inventory = Inventory.objects.filter(character=character)
        status = StatusPoints.objects.filter(character=character)

        character_serialized = serializers.CharacterSerializer(
            Character.objects.filter(user=user), many=True).data
        inventory_serialized = serializers.InventorySerializer(
            inventory, many=True).data
        status_serialized = serializers.StatusPointsSerializer(
            status, many=True).data

        # print(CharacterInformation(request).CharacterData())

        return Response({
            "character": character_serialized,
            "inventory": inventory_serialized,
            "status": status_serialized,
        })

    except:

        return Response({
            "message": "กรุณาลงชื่อเข้าใช้ระบบ หรือ ลงทะเบียน"
        })


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def getMonster(request):
    try:
        monster_list = serializers.MonsterSerializer(
            Monster.objects.all(), many=True).data
        return Response(monster_list)
    except:
        pass


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def Battle(request):
    print()
    char = CharacterInformation(request)
    monster = MonsterTarget(1)

    player = char.exportToBattle()
    target = monster.exportToBattle()

    # print(player, target)
    arena = ArenaBattle(player=player, target=target)

    p = arena.setPlayer()
    t = arena.setTarget()
    # print(p, t)

    return Response({"player": p, "playerRaw": player,  "target": t, "targetRaw": target})
