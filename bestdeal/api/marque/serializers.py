from rest_framework import serializers
from . models import Marque
from bestdeal.api.deal.serializers import DealsSerializer


class MarquesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = ('id', 'name')


class MarquesAllSerializer(serializers.ModelSerializer):
    deals = DealsSerializer(many=True, read_only=True)

    class Meta:
        model = Marque
        fields = ('id', 'name', 'deals')
