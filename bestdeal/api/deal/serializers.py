from rest_framework import serializers
from . models import Deal, Score
from . . commentaire.serializers import CommentSerializerNoFk
from . . user.serializers import UserSerializer
from django_countries.fields import CountryField
from django.db.models import Sum



class DealsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Deal
        fields = ('id', 'title', 'content')
        # fields = '__all__'
    
class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'

class DealsAllSerializer(serializers.HyperlinkedModelSerializer):
    country = CountryField()
    total_com = serializers.SerializerMethodField(read_only=True)
    total_sco = serializers.SerializerMethodField(read_only=True)
    user_add = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    dea_mar_fk = serializers.HyperlinkedRelatedField(view_name='marque-detail', read_only=True)

    def get_total_com(self, Comment):
        return Comment.com_deals.count()

    def get_total_sco(self, Score):
        totalsco = Score.sco_deals.aggregate(total_sco=Sum('score'))
        return totalsco["total_sco"]

    class Meta:
        model = Deal
        fields = '__all__'
        
class DealsCommentSerializer(serializers.ModelSerializer):
    country = CountryField()
    com_deals = CommentSerializerNoFk(many=True, read_only=True)
    total_com = serializers.SerializerMethodField(read_only=True)
    total_sco = serializers.SerializerMethodField(read_only=True)
    user_add = UserSerializer(read_only=True)

    def get_total_com(self, Comment):
        return Comment.com_deals.count()

    def get_total_sco(self, Score):
        totalsco = Score.sco_deals.aggregate(total_sco=Sum('score'))
        return totalsco["total_sco"]

    class Meta:
        model = Deal
        fields = '__all__'
    


