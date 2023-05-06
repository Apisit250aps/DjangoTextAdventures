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
        # self.uid = 2
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
        self.character_status_point = self.character.status_points

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
        
        if exp >= 0 and exp < 10:
            Character.objects.filter(user=self.user).update(levels=1)
        elif exp >= 10 and exp < 32:
            Character.objects.filter(user=self.user).update(levels=2)
        elif exp >= 32 and exp < 70:
            Character.objects.filter(user=self.user).update(levels=3)
        elif exp >= 70 and exp < 128:
            Character.objects.filter(user=self.user).update(levels=4)
        elif exp >= 128 and exp < 210:
            Character.objects.filter(user=self.user).update(levels=5)
        elif exp >= 210 and exp < 322:
            Character.objects.filter(user=self.user).update(levels=6)
        elif exp >= 322 and exp < 473:
            Character.objects.filter(user=self.user).update(levels=7)
        elif exp >= 473 and exp < 672:
            Character.objects.filter(user=self.user).update(levels=8)
        elif exp >= 672 and exp < 930:
            Character.objects.filter(user=self.user).update(levels=9)
        elif exp >= 930 and exp < 1262:
            Character.objects.filter(user=self.user).update(levels=10)
        elif exp >= 1262 and exp < 1688:
            Character.objects.filter(user=self.user).update(levels=11)
        elif exp >= 1688 and exp < 2230:
            Character.objects.filter(user=self.user).update(levels=12)
        elif exp >= 2230 and exp < 2917:
            Character.objects.filter(user=self.user).update(levels=13)
        elif exp >= 2917 and exp < 3787:
            Character.objects.filter(user=self.user).update(levels=14)
        elif exp >= 3787 and exp < 4884:
            Character.objects.filter(user=self.user).update(levels=15)
        elif exp >= 4884 and exp < 6265:
            Character.objects.filter(user=self.user).update(levels=16)
        elif exp >= 6265 and exp < 8001:
            Character.objects.filter(user=self.user).update(levels=17)
        elif exp >= 8001 and exp < 10182:
            Character.objects.filter(user=self.user).update(levels=18)
        elif exp >= 10182 and exp < 12917:
            Character.objects.filter(user=self.user).update(levels=19)
        elif exp >= 12917 and exp < 16347:
            Character.objects.filter(user=self.user).update(levels=20)
        elif exp >= 16347 and exp < 20644:
            Character.objects.filter(user=self.user).update(levels=21)
        elif exp >= 20644 and exp < 26025:
            Character.objects.filter(user=self.user).update(levels=22)
        elif exp >= 26025 and exp < 32761:
            Character.objects.filter(user=self.user).update(levels=23)
        elif exp >= 32761 and exp < 41191:
            Character.objects.filter(user=self.user).update(levels=24)
        elif exp >= 41191 and exp < 51739:
            Character.objects.filter(user=self.user).update(levels=25)
        elif exp >= 51739 and exp < 51947:
            Character.objects.filter(user=self.user).update(levels=26)
        elif exp >= 51947 and exp < 52163:
            Character.objects.filter(user=self.user).update(levels=27)
        elif exp >= 52163 and exp < 52387:
            Character.objects.filter(user=self.user).update(levels=28)
        elif exp >= 52387 and exp < 52619:
            Character.objects.filter(user=self.user).update(levels=29)
        elif exp >= 52619 and exp < 52859:
            Character.objects.filter(user=self.user).update(levels=30)
        elif exp >= 52859 and exp < 53107:
            Character.objects.filter(user=self.user).update(levels=31)
        elif exp >= 53107 and exp < 53363:
            Character.objects.filter(user=self.user).update(levels=32)
        elif exp >= 53363 and exp < 53627:
            Character.objects.filter(user=self.user).update(levels=33)
        elif exp >= 53627 and exp < 53899:
            Character.objects.filter(user=self.user).update(levels=34)
        elif exp >= 53899 and exp < 54179:
            Character.objects.filter(user=self.user).update(levels=35)
        elif exp >= 54179 and exp < 54467:
            Character.objects.filter(user=self.user).update(levels=36)
        elif exp >= 54467 and exp < 54763:
            Character.objects.filter(user=self.user).update(levels=37)
        elif exp >= 54763 and exp < 55067:
            Character.objects.filter(user=self.user).update(levels=38)
        elif exp >= 55067 and exp < 55379:
            Character.objects.filter(user=self.user).update(levels=39)
        elif exp >= 55379 and exp < 55699:
            Character.objects.filter(user=self.user).update(levels=40)
        elif exp >= 55699 and exp < 56027:
            Character.objects.filter(user=self.user).update(levels=41)
        elif exp >= 56027 and exp < 56363:
            Character.objects.filter(user=self.user).update(levels=42)
        elif exp >= 56363 and exp < 56707:
            Character.objects.filter(user=self.user).update(levels=43)
        elif exp >= 56707 and exp < 57059:
            Character.objects.filter(user=self.user).update(levels=44)
        elif exp >= 57059 and exp < 57419:
            Character.objects.filter(user=self.user).update(levels=45)
        elif exp >= 57419 and exp < 57787:
            Character.objects.filter(user=self.user).update(levels=46)
        elif exp >= 57787 and exp < 58163:
            Character.objects.filter(user=self.user).update(levels=47)
        elif exp >= 58163 and exp < 58547:
            Character.objects.filter(user=self.user).update(levels=48)
        elif exp >= 58547 and exp < 58939:
            Character.objects.filter(user=self.user).update(levels=49)
        elif exp >= 58939 and exp < 59339:
            Character.objects.filter(user=self.user).update(levels=50)
        elif exp >= 59339 and exp < 59747:
            Character.objects.filter(user=self.user).update(levels=51)
        elif exp >= 59747 and exp < 60163:
            Character.objects.filter(user=self.user).update(levels=52)
        elif exp >= 60163 and exp < 60587:
            Character.objects.filter(user=self.user).update(levels=53)
        elif exp >= 60587 and exp < 61019:
            Character.objects.filter(user=self.user).update(levels=54)
        elif exp >= 61019 and exp < 61459:
            Character.objects.filter(user=self.user).update(levels=55)
        elif exp >= 61459 and exp < 61907:
            Character.objects.filter(user=self.user).update(levels=56)
        elif exp >= 61907 and exp < 62363:
            Character.objects.filter(user=self.user).update(levels=57)
        elif exp >= 62363 and exp < 62827:
            Character.objects.filter(user=self.user).update(levels=58)
        elif exp >= 62827 and exp < 63299:
            Character.objects.filter(user=self.user).update(levels=59)
        elif exp >= 63299 and exp < 63779:
            Character.objects.filter(user=self.user).update(levels=60)
        elif exp >= 63779 and exp < 64267:
            Character.objects.filter(user=self.user).update(levels=61)
        elif exp >= 64267 and exp < 64763:
            Character.objects.filter(user=self.user).update(levels=62)
        elif exp >= 64763 and exp < 65267:
            Character.objects.filter(user=self.user).update(levels=63)
        elif exp >= 65267 and exp < 65779:
            Character.objects.filter(user=self.user).update(levels=64)
        elif exp >= 65779 and exp < 66299:
            Character.objects.filter(user=self.user).update(levels=65)
        elif exp >= 66299 and exp < 66827:
            Character.objects.filter(user=self.user).update(levels=66)
        elif exp >= 66827 and exp < 67363:
            Character.objects.filter(user=self.user).update(levels=67)
        elif exp >= 67363 and exp < 67907:
            Character.objects.filter(user=self.user).update(levels=68)
        elif exp >= 67907 and exp < 68459:
            Character.objects.filter(user=self.user).update(levels=69)
        elif exp >= 68459 and exp < 69019:
            Character.objects.filter(user=self.user).update(levels=70)
        elif exp >= 69019 and exp < 69587:
            Character.objects.filter(user=self.user).update(levels=71)
        elif exp >= 69587 and exp < 70163:
            Character.objects.filter(user=self.user).update(levels=72)
        elif exp >= 70163 and exp < 70747:
            Character.objects.filter(user=self.user).update(levels=73)
        elif exp >= 70747 and exp < 71339:
            Character.objects.filter(user=self.user).update(levels=74)
        elif exp >= 71339 and exp < 71939:
            Character.objects.filter(user=self.user).update(levels=75)
        elif exp >= 71939 and exp < 87057:
            Character.objects.filter(user=self.user).update(levels=76)
        elif exp >= 87057 and exp < 105207:
            Character.objects.filter(user=self.user).update(levels=77)
        elif exp >= 105207 and exp < 126998:
            Character.objects.filter(user=self.user).update(levels=78)
        elif exp >= 126998 and exp < 153156:
            Character.objects.filter(user=self.user).update(levels=79)
        elif exp >= 153156 and exp < 184555:
            Character.objects.filter(user=self.user).update(levels=80)
        elif exp >= 184555 and exp < 222243:
            Character.objects.filter(user=self.user).update(levels=81)
        elif exp >= 222243 and exp < 267479:
            Character.objects.filter(user=self.user).update(levels=82)
        elif exp >= 267479 and exp < 321772:
            Character.objects.filter(user=self.user).update(levels=83)
        elif exp >= 321772 and exp < 386933:
            Character.objects.filter(user=self.user).update(levels=84)
        elif exp >= 386933 and exp < 465136:
            Character.objects.filter(user=self.user).update(levels=85)
        elif exp >= 465136 and exp < 558989:
            Character.objects.filter(user=self.user).update(levels=86)
        elif exp >= 558989 and exp < 671622:
            Character.objects.filter(user=self.user).update(levels=87)
        elif exp >= 671622 and exp < 806791:
            Character.objects.filter(user=self.user).update(levels=88)
        elif exp >= 806791 and exp < 969004:
            Character.objects.filter(user=self.user).update(levels=89)
        elif exp >= 969004 and exp < 1163668:
            Character.objects.filter(user=self.user).update(levels=90)
        elif exp >= 1163668 and exp < 1280836:
            Character.objects.filter(user=self.user).update(levels=91)
        elif exp >= 1280836 and exp < 1409729:
            Character.objects.filter(user=self.user).update(levels=92)
        elif exp >= 1409729 and exp < 1551521:
            Character.objects.filter(user=self.user).update(levels=93)
        elif exp >= 1551521 and exp < 1707500:
            Character.objects.filter(user=self.user).update(levels=94)
        elif exp >= 1707500 and exp < 1879086:
            Character.objects.filter(user=self.user).update(levels=95)
        elif exp >= 1879086 and exp < 2067839:
            Character.objects.filter(user=self.user).update(levels=96)
        elif exp >= 2067839 and exp < 2275477:
            Character.objects.filter(user=self.user).update(levels=97)
        elif exp >= 2275477 and exp < 2503887:
            Character.objects.filter(user=self.user).update(levels=98)
        elif exp >= 2503887 and exp < 2755147:
            Character.objects.filter(user=self.user).update(levels=99)
        elif exp >= 2755147:
            Character.objects.filter(user=self.user).update(levels=100)




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
