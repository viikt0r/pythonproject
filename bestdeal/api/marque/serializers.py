from rest_framework import serializers
from . models import Marque
#from . . deal.serializers import DealsAllSerializer
from . . user.serializers import UserSerializer

class MarquesSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')
    
    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')


class MarquesAllSerializer(serializers.HyperlinkedModelSerializer):
    #dea_marques = DealsAllSerializer(many=True, read_only=True)
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'dea_marques', 'user_add')
        depth = 1

class MarquesSimpleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Marque
        fields = ('url', 'id', 'name')

    


