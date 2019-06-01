from rest_framework import generics, mixins, permissions
from . serializers import UserSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detail d'un user"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    #authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
