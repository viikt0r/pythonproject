from rest_framework import serializers
from . models import Deal, Score, Follow
from . . commentaire.serializers import CommentSerializerNoFk
from . . user.serializers import UserSerializer
from . . marque.serializers import MarquesSimpleSerializer
from . . tag.serializers import TagSerializer
from . . tag.models import Tag
from . . marque.models import Marque
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models import Sum


class DealsSerializer(serializers.HyperlinkedModelSerializer):
    country = CountryField()
    nb_comment = serializers.SerializerMethodField(read_only=True)
    moyenne_vote = serializers.SerializerMethodField(read_only=True)
    user_add = serializers.ReadOnlyField(source='user_add.username')
    marques = MarquesSimpleSerializer(read_only=True, source='dea_mar_fk')
    tags = TagSerializer(many=True, read_only=True, source='tag_set')

    def get_nb_comment(self, Comment):
        return Comment.com_deals.count()

    def get_moyenne_vote(self, Score):
        totalsco = Score.sco_deals.aggregate(moyenne_vote=Sum('score'))
        return totalsco["moyenne_vote"]

    class Meta:
        model = Deal
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'


class DealsAllSerializer(serializers.HyperlinkedModelSerializer):
    country = CountryField()
    nb_comment = serializers.SerializerMethodField(read_only=True)
    moyenne_vote = serializers.SerializerMethodField(read_only=True)
    user_add = serializers.ReadOnlyField(source='user_add.username')
    marques = MarquesSimpleSerializer(read_only=True, source='dea_mar_fk')

    def get_nb_comment(self, Comment):
        return Comment.com_deals.count()

    def get_moyenne_vote(self, Score):
        totalsco = Score.sco_deals.aggregate(moyenne_vote=Sum('score'))
        return totalsco["moyenne_vote"]

    class Meta:
        model = Deal
        fields = '__all__'


class DealsCommentSerializer(serializers.HyperlinkedModelSerializer):

    com_deals = CommentSerializerNoFk(many=True, read_only=True)
    nb_comment = serializers.SerializerMethodField(read_only=True)

    def get_nb_comment(self, Comment):
        return Comment.com_deals.count()

    class Meta:
        model = Deal
        fields = ('url', 'id', 'nb_comment', 'com_deals')


class TagAllSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tag-detail")
    nb_deals = serializers.SerializerMethodField(read_only=True)
    dea_tags = DealsSerializer(many=True, read_only=True)

    def get_nb_deals(self, Deal):
        return Deal.dea_tags.count()

    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', 'photo', 'main', 'nb_deals', 'dea_tags')


class UserAllSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    nb_deals = serializers.SerializerMethodField(read_only=True)
    dea_users = DealsSerializer(many=True, read_only=True)

    def get_nb_deals(self, Deal):
        return Deal.dea_users.count()

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'nb_deals', 'dea_users')


class FollowSerializer(serializers.ModelSerializer):
    deals = DealsSerializer(read_only=True, source='fol_dea_fk')
    users = UserSerializer(read_only=True, source='user_follow')

    class Meta:
        model = Follow
        fields = '__all__'


class UserFollowSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    follow_users = FollowSerializer(many=True, read_only=True)
    nb_deals = serializers.SerializerMethodField(read_only=True)

    def get_nb_deals(self, obj):
        return obj.follow_users.count()

    class Meta:
        model = User
        fields = ('url', 'id', 'nb_deals', 'username', 'follow_users')


class MarqueAllSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="marque-detail")
    nb_deals = serializers.SerializerMethodField(read_only=True)
    dea_marques = DealsSerializer(many=True, read_only=True)

    def get_nb_deals(self, Deal):
        return Deal.dea_marques.count()

    class Meta:
        model = Marque
        fields = ('url', 'id', 'name', 'photo', 'link',
                  'user_add', 'nb_deals', 'dea_marques')
