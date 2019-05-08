from rest_framework import generics, mixins, permissions
from . models import AbuseReport
from . serializers import AbuseSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly

class AbuseListView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = AbuseSerializer

    def get_queryset(self):
        qs = AbuseReport.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AbuseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = AbuseSerializer

    def get_queryset(self):
        return AbuseReport.objects.all()