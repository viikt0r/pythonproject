from rest_framework import generics, mixins, permissions
from . serializers import UserSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()