from rest_framework import serializers
from . models import Deal
# from bestdeal.api.marque.serializers import MarquesSerializer


class DealsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = ('id', 'title', 'content')
        # fields = '__all__'


class DealsAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = '__all__'

