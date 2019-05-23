from rest_framework import serializers
from . models import AbuseReport
from . . user.serializers import UserSerializer


class AbuseSerializer(serializers.HyperlinkedModelSerializer):
    user_add = UserSerializer(read_only=True)

    class Meta:
        model = AbuseReport
        fields = '__all__'