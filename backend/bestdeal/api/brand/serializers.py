from rest_framework import serializers
from . models import Brand
from . . user.serializers import UserSerializer


class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Brand
        fields = ('url', 'id', 'name', 'photo', 'link', 'user_add')


class BrandsSimpleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = ('url', 'id', 'name')
