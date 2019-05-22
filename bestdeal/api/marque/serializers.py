from rest_framework import serializers
from . models import Marque
from . . user.serializers import UserSerializer

class MarquesSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')
    
    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')


class MarquesAllSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'deal_marque', 'user_add')
        #fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')
        depth = 1

class MarquesSimpleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Marque
        fields = ('url', 'id', 'name')

    


