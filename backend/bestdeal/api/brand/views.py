from rest_framework import generics, mixins, permissions
from . models import Brand
from . serializers import BrandsSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from django.core.files.storage import FileSystemStorage


class BrandListView(mixins.CreateModelMixin, generics.ListAPIView):
    """Liste des marques avec la possibilité de faire une recherche"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    id = 'pk'
    serializer_class = BrandsSerializer

    def get_queryset(self):
        qs = Brand.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(mar_nom=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        #photo = request.FILES['photo']
        #fs = FileSystemStorage()
        #filename = fs.save(photo.name, photo)
        return self.create(request, *args, **kwargs)


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detail d'une marque"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    id = 'pk'
    serializer_class = BrandsSerializer

    def get_queryset(self):
        return Brand.objects.all()
