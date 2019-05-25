from rest_framework import serializers
from . models import Marque
from . . user.serializers import UserSerializer


class MarquesSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')


class MarquesSimpleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name')
