from rest_framework import generics, mixins, permissions
from . models import Tag
from . serializers import TagSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from . . deal.serializers import TagAllSerializer

class TagListView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    Liste des tags avec la possibilité de faire une recherche
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = TagSerializer

    def get_queryset(self):
        qs = Tag.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(tag_nom=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Détail d'un tag
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()


