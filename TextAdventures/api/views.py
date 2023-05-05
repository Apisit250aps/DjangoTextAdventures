
import time
from asgiref.sync import sync_to_async
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

import pandas as pds

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
@api_view(["GET",])
@permission_classes((AllowAny,))
def getLog(request):

    log = {
        "attacker": [],
        "attack_status": [],
        "protector": [],
        "damage": []
    }

    for logs in Battle_log.objects.all():
        log["attacker"].append(logs.attacker)
        log["attack_status"].append(logs.attack_status)
        log["protector"].append(logs.protector)
        log["damage"].append(logs.damage)

    battle_logs = pds.DataFrame(log)

    try:
        with pds.ExcelWriter('Battle_log.xlsx') as writer:
            battle_logs.to_excel(writer, sheet_name="battle_logs", index=None)

        status = True
    except:
        status = False

    return Response({"status": status, "file": finders('Battle_log.xlsx')})


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
    CharacterInformation(request).setLevel()
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


async def printf():
    await print("love")


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny,))
def Battle(request):
    print()
    _player = CharacterInformation(request)
    _monster = MonsterTarget(2)

    energy = Character.objects.get(user=_player.user)
    print(energy.energy)
    if energy.energy >= 3:
        Character.objects.filter(user=_player.user).update(
            energy=energy.energy-3)
        player = _player.exportToBattle()
        target = _monster.exportToBattle()

        # print(player, target)
        arena = ArenaBattle(player=_player.exportToBattle(),
                            target=_monster.exportToBattle())

        battle = arena.BattleArena()
        if battle['winner'] == 'player':
            exp_drop = int(_monster.exp_drop)
            gold_drop = int(_monster.gold_drop)

            print('exp drop', exp_drop)
            player_exp = int(_player.character_exp) + exp_drop
            player_gold = int(_player.character_gold + gold_drop)
            # print(player_exp)
            Character.objects.filter(user=_player.uid).update(
                exp=player_exp, gold=player_gold)

        level_before = CharacterInformation(request).character_levels

        CharacterInformation(request).setLevel()

        level_after = CharacterInformation(request).character_levels
        statusPoint_character = CharacterInformation(
            request).character_status_point

        if level_after > level_before:
            print("Level Up")
            statusPoint_character += 3
            Character.objects.filter(user=_player.uid).update(
                status_points=statusPoint_character)

        else:
            print("Not Up")
        
        return Response({"status":True ,"battle": battle, "energy":Character.objects.get(user=_player.user).energy})
    
    else :
        

        print(Character.objects.get(user=_player.user).energy)

        return Response({"status":False,"battle": "your tire", "energy":Character.objects.get(user=_player.user).energy})
