from rest_framework import serializers
from . models import Marque
from . . deal.serializers import DealsAllSerializer, DealsSerializer
from . . user.serializers import UserSerializer

class MarquesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="marque-detail")
    user_add = serializers.ReadOnlyField(source='user_add.username')
    
    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')


class MarquesAllSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="marque-detail")
    dea_marques = DealsAllSerializer(many=True, read_only=True)
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'dea_marques', 'user_add')



    


