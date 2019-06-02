from rest_framework import generics, mixins, permissions
from . models import Deal, Score, Follow
from . . tag.models import Tag
from . . brand.models import Brand
from . serializers import *
#from . serializers import DealsAllSerializer, DealsSerializer, DealsCommentSerializer, ScoreSerializer, TagAllSerializer, UserAllSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.contrib.auth.models import User


class DealListView(mixins.CreateModelMixin, generics.ListAPIView):
    """Liste des deals avec la possibilité de faire une recherche"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    id = 'pk'
    serializer_class = DealsAllSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('updated_at',)
    ordering = ('updated_at',)

    def get_queryset(self):
        qs = Deal.objects.all().prefetch_related('tag_set')
        query = self.request.GET.get("q")  # ?q=ipad par exemple dans lurl
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).distinct()
            print (qs.query)
        return qs

    def perform_create(self, serializer):
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detail d'un deal"""
    permission_classes = (IsAuthenticated,)
    id = 'pk'
    serializer_class = DealsSerializer

    def get_queryset(self):
        return Deal.objects.all()


class DealNoFk(generics.ListAPIView):
    id = 'pk'
    queryset = Deal.objects.all()
    serializer_class = DealsSerializer


class DealCommentDetailView(generics.RetrieveAPIView):
    """Liste des commentaires pour un deal"""
    id = 'pk'
    serializer_class = DealsCommentSerializer

    def get_queryset(self):
        return Deal.objects.all()


class ScoreListView(mixins.CreateModelMixin, generics.ListAPIView):
    id = 'pk'
    serializer_class = ScoreSerializer

    def get_queryset(self):
        qs = Score.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(score=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDeals(generics.RetrieveAPIView):
    """
    Liste des deals pour un tag
    """
    id = 'pk'
    serializer_class = TagAllSerializer

    def get_queryset(self):
        return Tag.objects.all()


class UserDeals(generics.RetrieveAPIView):
    """
    Liste des deals pour un user
    """
    id = 'pk'
    serializer_class = UserAllSerializer

    def get_queryset(self):
        return User.objects.all()


class UserFollowDeals(generics.RetrieveAPIView):
    """
    Liste des deals qui sont follow pour un user
    """
    id = 'pk'
    serializer_class = UserFollowSerializer

    def get_queryset(self):
        # return Follow.objects.all().filter(user_follow=self.request.user)
        return User.objects.all()


class FollowListView(mixins.CreateModelMixin, generics.ListAPIView):
    id = 'pk'
    serializer_class = FollowSerializer

    def get_queryset(self):
        qs = Follow.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BrandDeals(generics.RetrieveAPIView):
    """
    Liste des deals pour une marque
    """
    id = 'pk'
    serializer_class = BrandAllSerializer

    def get_queryset(self):
        return Brand.objects.all()

#from django.db.models import Sum
#all_sum = transaction.aggregate(Sum('amount'))['amount__sum']
# return Response({'sum': all_sum if all_sum else 0 , 'objects': serializer.data})
