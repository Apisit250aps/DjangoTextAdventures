from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Character)
class Character(admin.ModelAdmin):
    list_display = [
        'user',
        'character_name',
        'levels',
        'gold'
    ]


@admin.register(models.StatusPoints)
class StatusPoints(admin.ModelAdmin):
    list_display = [
        "character",
        "str",
        "vit",
        "agi"
    ]


@admin.register(models.Inventory)
class Inventory(admin.ModelAdmin):
    list_display = [
        "character",
        "items_id",
        "unit"
    ]


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'category',
        'price',

    ]


@admin.register(models.Monster)
class Monster(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'levels',
        'health',
        'attack',
        'defense'
    ]


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = [
        'title',
        'target',
        'unit',
        'reward_type',
        'reward_unit'
    ]
