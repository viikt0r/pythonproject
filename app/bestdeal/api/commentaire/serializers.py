from rest_framework import serializers
from . models import Comment
from . . user.serializers import UserSerializer


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user_add = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializerNoFk(serializers.HyperlinkedModelSerializer):
    user_add = serializers.ReadOnlyField(source='user_add.username')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'text', 'approved_comment', 'created_at', 'updated_at', 'user_add')
        