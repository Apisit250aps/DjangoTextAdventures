import time
from random import random
from typing import Any
from django.contrib.auth.models import User
from .models import *
from .serializers import *
import random as rd


class CharacterInformation:
    def __init__(self, request):
        self.uid = request.session["_auth_user_id"]
        # self.uid = 1
        self.user = User.objects.get(id=self.uid)
        self.character = Character.objects.get(user=self.user)
        self.inventory = Inventory.objects.filter(character=self.character)
        self.status = StatusPoints.objects.get(character=self.character)

        self.base_health = int(
            self.character.health+((self.character.health/3)*(self.character.levels*self.status.vit)))
        self.base_attack = int(
            self.character.attack+((self.character.attack/2.5)*(self.character.levels*self.status.str)))
        self.base_defense = int(
            self.character.defense+(
                (self.character.defense/3.5)*(self.character.levels*(self.status.vit/0.75))))
        self.base_speed = int(self.character.speed*self.status.agi*0.0393)

        #
        self.character_name = self.character.character_name
        self.character_gold = self.character.gold
        self.character_exp = self.character.exp
        self.character_levels = self.character.levels

    def exportToBattle(self):
        statusValue = {
            'name': self.character_name,
            'health': self.base_health,
            'attack': self.base_attack,
            'defense': self.base_defense,
            'speed': self.base_speed,
        }

        return statusValue

    def inventories(self):
        inventory = []

        for item in self.inventory:
            items = Item.objects.get(id=item.items_id)
            item_get = {

            }
            item_get['name'] = items.name
            item_get['img'] = items.img
            item_get['damage'] = items.damage
            item_get['defense'] = items.defense
            item_get['category'] = items.category
            item_get['price'] = items.price

            inventory.append(item_get)
        return inventory

    def setLevel(self):

        exp = self.character_exp
        print(f"exp : {exp}")
        if exp >= 10000000000:
            Character.objects.filter(user=self.user).update(levels=100)
        elif exp >= 9900000000:
            Character.objects.filter(user=self.user).update(levels=99)
        elif exp >= 9800000000:
            Character.objects.filter(user=self.user).update(levels=98)
        elif exp >= 9700000000:
            Character.objects.filter(user=self.user).update(levels=97)
        elif exp >= 9600000000:
            Character.objects.filter(user=self.user).update(levels=96)
        elif exp >= 9500000000:
            Character.objects.filter(user=self.user).update(levels=95)
        elif exp >= 9400000000:
            Character.objects.filter(user=self.user).update(levels=94)
        elif exp >= 9300000000:
            Character.objects.filter(user=self.user).update(levels=93)
        elif exp >= 9200000000:
            Character.objects.filter(user=self.user).update(levels=92)
        elif exp >= 9100000000:
            Character.objects.filter(user=self.user).update(levels=91)
        elif exp >= 9000000000:
            Character.objects.filter(user=self.user).update(levels=90)
        elif exp >= 8900000000:
            Character.objects.filter(user=self.user).update(levels=89)
        elif exp >= 8800000000:
            Character.objects.filter(user=self.user).update(levels=88)
        elif exp >= 8700000000:
            Character.objects.filter(user=self.user).update(levels=87)
        elif exp >= 8600000000:
            Character.objects.filter(user=self.user).update(levels=86)
        elif exp >= 8500000000:
            Character.objects.filter(user=self.user).update(levels=85)
        elif exp >= 8400000000:
            Character.objects.filter(user=self.user).update(levels=84)
        elif exp >= 8300000000:
            Character.objects.filter(user=self.user).update(levels=83)
        elif exp >= 8200000000:
            Character.objects.filter(user=self.user).update(levels=82)
        elif exp >= 8100000000:
            Character.objects.filter(user=self.user).update(levels=81)
        elif exp >= 800000000:
            Character.objects.filter(user=self.user).update(levels=80)
        elif exp >= 790000000:
            Character.objects.filter(user=self.user).update(levels=79)
        elif exp >= 780000000:
            Character.objects.filter(user=self.user).update(levels=78)
        elif exp >= 770000000:
            Character.objects.filter(user=self.user).update(levels=77)
        elif exp >= 760000000:
            Character.objects.filter(user=self.user).update(levels=76)
        elif exp >= 750000000:
            Character.objects.filter(user=self.user).update(levels=75)
        elif exp >= 740000000:
            Character.objects.filter(user=self.user).update(levels=74)
        elif exp >= 730000000:
            Character.objects.filter(user=self.user).update(levels=73)
        elif exp >= 720000000:
            Character.objects.filter(user=self.user).update(levels=72)
        elif exp >= 710000000:
            Character.objects.filter(user=self.user).update(levels=71)
        elif exp >= 700000000:
            Character.objects.filter(user=self.user).update(levels=70)
        elif exp >= 690000000:
            Character.objects.filter(user=self.user).update(levels=69)
        elif exp >= 680000000:
            Character.objects.filter(user=self.user).update(levels=68)
        elif exp >= 670000000:
            Character.objects.filter(user=self.user).update(levels=67)
        elif exp >= 660000000:
            Character.objects.filter(user=self.user).update(levels=66)
        elif exp >= 650000000:
            Character.objects.filter(user=self.user).update(levels=65)
        elif exp >= 640000000:
            Character.objects.filter(user=self.user).update(levels=64)
        elif exp >= 630000000:
            Character.objects.filter(user=self.user).update(levels=63)
        elif exp >= 620000000:
            Character.objects.filter(user=self.user).update(levels=62)
        elif exp >= 610000000:
            Character.objects.filter(user=self.user).update(levels=61)
        elif exp >= 60000000:
            Character.objects.filter(user=self.user).update(levels=60)
        elif exp >= 59000000:
            Character.objects.filter(user=self.user).update(levels=59)
        elif exp >= 58000000:
            Character.objects.filter(user=self.user).update(levels=58)
        elif exp >= 57000000:
            Character.objects.filter(user=self.user).update(levels=57)
        elif exp >= 56000000:
            Character.objects.filter(user=self.user).update(levels=56)
        elif exp >= 55000000:
            Character.objects.filter(user=self.user).update(levels=55)
        elif exp >= 54000000:
            Character.objects.filter(user=self.user).update(levels=54)
        elif exp >= 53000000:
            Character.objects.filter(user=self.user).update(levels=53)
        elif exp >= 52000000:
            Character.objects.filter(user=self.user).update(levels=52)
        elif exp >= 51000000:
            Character.objects.filter(user=self.user).update(levels=51)
        elif exp >= 5000000:
            Character.objects.filter(user=self.user).update(levels=50)
        elif exp >= 4900000:
            Character.objects.filter(user=self.user).update(levels=49)
        elif exp >= 4800000:
            Character.objects.filter(user=self.user).update(levels=48)
        elif exp >= 4700000:
            Character.objects.filter(user=self.user).update(levels=47)
        elif exp >= 4600000:
            Character.objects.filter(user=self.user).update(levels=46)
        elif exp >= 4500000:
            Character.objects.filter(user=self.user).update(levels=45)
        elif exp >= 4400000:
            Character.objects.filter(user=self.user).update(levels=44)
        elif exp >= 4300000:
            Character.objects.filter(user=self.user).update(levels=43)
        elif exp >= 4200000:
            Character.objects.filter(user=self.user).update(levels=42)
        elif exp >= 4100000:
            Character.objects.filter(user=self.user).update(levels=41)
        elif exp >= 400000:
            Character.objects.filter(user=self.user).update(levels=40)
        elif exp >= 390000:
            Character.objects.filter(user=self.user).update(levels=39)
        elif exp >= 380000:
            Character.objects.filter(user=self.user).update(levels=38)
        elif exp >= 370000:
            Character.objects.filter(user=self.user).update(levels=37)
        elif exp >= 360000:
            Character.objects.filter(user=self.user).update(levels=36)
        elif exp >= 350000:
            Character.objects.filter(user=self.user).update(levels=35)
        elif exp >= 340000:
            Character.objects.filter(user=self.user).update(levels=34)
        elif exp >= 330000:
            Character.objects.filter(user=self.user).update(levels=33)
        elif exp >= 320000:
            Character.objects.filter(user=self.user).update(levels=32)
        elif exp >= 310000:
            Character.objects.filter(user=self.user).update(levels=31)
        elif exp >= 30000:
            Character.objects.filter(user=self.user).update(levels=30)
        elif exp >= 29000:
            Character.objects.filter(user=self.user).update(levels=29)
        elif exp >= 28000:
            Character.objects.filter(user=self.user).update(levels=28)
        elif exp >= 27000:
            Character.objects.filter(user=self.user).update(levels=27)
        elif exp >= 26000:
            Character.objects.filter(user=self.user).update(levels=26)
        elif exp >= 25000:
            Character.objects.filter(user=self.user).update(levels=25)
        elif exp >= 24000:
            Character.objects.filter(user=self.user).update(levels=24)
        elif exp >= 23000:
            Character.objects.filter(user=self.user).update(levels=23)
        elif exp >= 22000:
            Character.objects.filter(user=self.user).update(levels=22)
        elif exp >= 21000:
            Character.objects.filter(user=self.user).update(levels=21)
        elif exp >= 2000:
            Character.objects.filter(user=self.user).update(levels=20)
        elif exp >= 1900:
            Character.objects.filter(user=self.user).update(levels=19)
        elif exp >= 1800:
            Character.objects.filter(user=self.user).update(levels=18)
        elif exp >= 1700:
            Character.objects.filter(user=self.user).update(levels=17)
        elif exp >= 1600:
            Character.objects.filter(user=self.user).update(levels=16)
        elif exp >= 1500:
            Character.objects.filter(user=self.user).update(levels=15)
        elif exp >= 1400:
            Character.objects.filter(user=self.user).update(levels=14)
        elif exp >= 1300:
            Character.objects.filter(user=self.user).update(levels=13)
        elif exp >= 1200:
            Character.objects.filter(user=self.user).update(levels=12)
        elif exp >= 1100:
            Character.objects.filter(user=self.user).update(levels=11)
        elif exp >= 100:
            Character.objects.filter(user=self.user).update(levels=10)
        elif exp >= 90:
            Character.objects.filter(user=self.user).update(levels=9)
        elif exp >= 80:
            Character.objects.filter(user=self.user).update(levels=8)
        elif exp >= 70:
            Character.objects.filter(user=self.user).update(levels=7)
        elif exp >= 60:
            Character.objects.filter(user=self.user).update(levels=6)
        elif exp >= 50:
            Character.objects.filter(user=self.user).update(levels=5)
        elif exp >= 40:
            Character.objects.filter(user=self.user).update(levels=4)
        elif exp >= 30:
            Character.objects.filter(user=self.user).update(levels=3)
        elif exp >= 20:
            Character.objects.filter(user=self.user).update(levels=2)
        elif exp >= 10:
            Character.objects.filter(user=self.user).update(levels=1)



    # print(f"now is {Character.objects.filter(user=self.user).level}")


class MonsterTarget():

    def __init__(self, monster_id):
        self.monster = Monster.objects.get(id=monster_id)
        self.monster_name = self.monster.name
        self.exp_drop = int(self.monster.exp_drop)
        self.gold_drop = int(self.monster.gold_drop)

    def exportToBattle(self):
        statusValue = {
            'name': self.monster_name,
            'health': self.monster.health,
            'attack': self.monster.attack,
            'defense': self.monster.defense,
            'speed': self.monster.speed,
        }

        return statusValue


class ArenaBattle():

    def __init__(self, player: dict, target: dict):
        self.player = player
        self.playerDied = False
        self.target = target
        self.targetDied = False
        self.battle_log = list()

    def setPlayer(self):

        def setRange(value):
            return rd.randrange(int(value-(value*0.05)), int(value+(value*0.05)))

        def randomDoge(value):
            speed = value/100
            return random() <= speed

        return {
            "name": self.player['name'],
            "attackRange": setRange(self.player['attack']),
            "defenseRange": setRange(self.player['defense']),
            "doge": randomDoge(self.player['speed'])
        }

    def setTarget(self):
        def setRange(value):
            return rd.randrange(int(value-(value*0.05)), int(value+(value*0.05)))

        def randomDoge(value):
            speed = value/100
            return random() <= speed

        return {
            "name": self.target['name'],
            "attackRange": setRange(self. target['attack']),
            "defenseRange": setRange(self.target['defense']),
            "doge": randomDoge(self.target['speed'])
        }

    def duelState(self, attacker: dict, protector: dict):
        damage = attacker['attackRange']
        doge = protector['doge']
        guards = protector['defenseRange']
        b_log = ""

        attack = True

        if not doge:
            damage -= (guards*0.3)
            if damage <= 0:
                damage = int(attacker['attackRange'])*0.1
            attack = True
            b_log = f"{attacker['name']} has attack {protector['name']} damage {int(damage)}!"

        else:
            attack = False
            damage = 0
            b_log = f"{attacker['name']} attack miss!"

        Battle_log.objects.create(
            attacker=attacker['name'], attack_status=attack, protector=protector['name'], damage=damage)

        return {"battle_log": b_log, "damage": int(damage)}

    def log_writer(self):
        pass

    def BattleArena(self):
        turn = 1
        winner = ''
        Battle = True
        while Battle:
            # time.sleep(0.5)
            _player = self.setPlayer()
            _target = self.setTarget()

            playerAttack = self.duelState(attacker=_player, protector=_target)
            self.battle_log.append(playerAttack['battle_log'])
            print(playerAttack['battle_log'])
            self.target['health'] -= playerAttack['damage']
            print(f"target : {self.target['health']}")

            if self.target['health'] <= 0:
                winner = 'player'
                Battle = False
            else:
                targetAttack = self.duelState(
                    attacker=_target, protector=_player)
                self.battle_log.append(targetAttack['battle_log'])
                print(targetAttack['battle_log'])
                self.player['health'] -= targetAttack['damage']
                print(f"player : {self.player['health']}")
                if self.player['health'] <= 0:
                    winner = 'target'
                    Battle = False
                else:
                    continue

        return {"log": self.battle_log, "winner": winner}
