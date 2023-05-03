from rest_framework import serializers
from .models import *

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        
class StatusPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPoints
        fields = '__all__'
        
class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'