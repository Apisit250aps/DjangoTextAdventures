from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CAT_CHOICES = (
    (1, 'weapon'),
    (2, 'armor')
)

REWARD_CHOICE = (
    (1, 'exp'),
    (2, 'gold')
)


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    img = models.ImageField(blank=True)
    attack = models.IntegerField(default=10, blank=True)
    health = models.IntegerField(default=100, blank=True)
    defense = models.IntegerField(default=100, blank=True)
    levels = models.IntegerField(default=1, blank=True)
    gold = models.IntegerField(default=0, blank=True)
    status_points = models.IntegerField(default=10, blank=True)
    
    def __str__(self):
        return self.name


class StatusPoints(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    str = models.IntegerField(default=1)
    vit = models.IntegerField(default=1)
    agi = models.IntegerField(default=1)


class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    items_id = models.IntegerField(blank=True)
    unit = models.IntegerField(default=0)


class Item(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(blank=True)
    damage = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    category = models.IntegerField(choices=CAT_CHOICES)
    price = models.IntegerField()


class Monster(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(blank=True)
    levels = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    exp_drop = models.IntegerField(default=0)


class Question(models.Model):
    title = models.CharField(max_length=64)
    detail = models.TextField(max_length=128)
    target = models.CharField(max_length=64)
    unit = models.IntegerField()
    reward_type = models.IntegerField(choices=REWARD_CHOICE)
    reward_unit = models.IntegerField()
