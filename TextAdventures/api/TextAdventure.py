from django.contrib.auth.models import User
from .models import *
from .serializers import *


class TextAdventures:
    def __init__(self, request):
        self.uid = request.session["_auth_user_id"]
        self.user = User.objects.get(id=self.uid)
        # self.character_info = 
        

    def CharacterData(self):
        
        return self.user
    
    def allMonsters(self):
        monster_list = MonsterSerializer(Monster.objects.all(), many=True).data
        return monster_list
    
    def getMonster(self, id):
        monster = Monster.objects.get(id=id)
        return monster
