from random import random
from typing import Any
from django.contrib.auth.models import User
from .models import *
from .serializers import *
import random as rd


class CharacterInformation:
    def __init__(self, request):
        self.uid = request.session["_auth_user_id"]
        self.user = User.objects.get(id=self.uid)
        self.character = Character.objects.get(user=self.user)
        self.inventory = Inventory.objects.filter(character=self.character)
        self.status = StatusPoints.objects.get(character=self.character)

        self.base_health = int(
            self.character.health+((self.character.health/3)*(self.character.levels*self.status.vit)))
        self.base_attack = int(
            self.character.attack+((self.character.attack/2.5)*(self.character.levels*self.status.str)))
        self.base_defense = int(self.character.defense+(
            (self.character.defense/3.5)*(self.character.levels*(self.status.vit/0.75))))
        self.base_speed = int(self.character.speed*self.status.agi*0.0393)

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


class MonsterTarget():

    def __init__(self, monster_id):
        self.monster = Monster.objects.get(id=monster_id)

        self.monster_name = self.monster.name
        self.exp_drop = self.monster.exp_drop
        self.gold_drop = self.monster.gold_drop

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
        self.target = target

    def setPlayer(self):

        def setRange(value):

            return rd.randrange(int(value-(value*0.05)), int(value+(value*0.05)))

        def randomDoge(value):
            speed = value/100
            doge = False
            if random() <= speed:
                doge = True

            return doge

        return {
            "attackRange": setRange(self.player['attack']),
            "defenseRange": setRange(self.player['defense']),
            "doge": randomDoge(self.player['speed'])
        }

    def setTarget(self):
        def setRange(value):

            return rd.randrange(int(value-(value*0.05)), int(value+(value*0.05)))

        def randomDoge(value):
            speed = value/100
            doge = False
            if random() <= speed:
                doge = True

            return doge

        return {
            "attackRange": setRange(self. target['attack']),
            "defenseRange": setRange(self.target['defense']),
            "doge": randomDoge(self.target['speed'])
        }
