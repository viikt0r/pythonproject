from rest_framework import serializers
from . models import Comment
from . . user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user_add = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializerNoFk(serializers.ModelSerializer):
    user_add = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'approved_comment', 'created_at', 'updated_at', 'user_add')
        