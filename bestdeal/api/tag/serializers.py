from rest_framework import serializers
from . models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at', 'updated_at')

    # def to_representation(self, instance):
        # return instance.tag_nom
