from rest_framework import serializers
from . models import Tag

class TagSerializer(serializers.HyperlinkedModelSerializer):
    #user_add = serializers.ReadOnlyField(source='user_add.username')
    
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', 'photo', 'main')

