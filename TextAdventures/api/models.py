from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    (1, 'weapon'),
    (2, 'armor'),
    (3, 'items')
)

REWARD_CHOICE = (
    (1, 'exp'),
    (2, 'gold'),
    (3, 'items')
)


class Character(models.Model):
    # General
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=64, unique=True)
    img = models.ImageField(blank=True)

    # Status
    health = models.IntegerField(default=100, blank=True)
    attack = models.IntegerField(default=10, blank=True)
    defense = models.IntegerField(default=10, blank=True)
    speed = models.IntegerField(default=10)
    levels = models.IntegerField(default=1, blank=True)
    exp = models.IntegerField(default=0)
    gold = models.IntegerField(default=0, blank=True)
    status_points = models.IntegerField(default=10, blank=True)

    def __str__(self):
        return self.character_name


class StatusPoints(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    str = models.IntegerField(default=1)
    vit = models.IntegerField(default=1)
    agi = models.IntegerField(default=1)


class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    items_id = models.IntegerField(blank=True)
    unit = models.IntegerField(default=1)


class Item(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField(blank=True)
    damage = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    price = models.IntegerField(default=0)


class Monster(models.Model):
    # General
    name = models.CharField(max_length=64)
    img = models.ImageField(blank=True)
    # Status
    levels = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    # Rewards
    exp_drop = models.IntegerField(default=0)
    gold_drop = models.IntegerField(default=0)
    items_drop = models.BooleanField(default=False)


class Question(models.Model):
    title = models.CharField(max_length=64)
    detail = models.TextField(max_length=128)
    target = models.CharField(max_length=64)
    unit = models.IntegerField()
    reward_type = models.IntegerField(choices=REWARD_CHOICE)
    reward_unit = models.IntegerField()
    reward_id = models.IntegerField()
