from rest_framework import serializers
from . models import Tag
#from . . . api.deal.serializers import DealsAllSerializer

class TagSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')
    
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', 'photo', 'main', 'user_add')

    # def to_representation(self, instance):
        # return instance.tag_nom

class TagAllSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tag-detail")
    #dea_tags = DealsAllSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', 'photo', 'main', 'dea_tags')
