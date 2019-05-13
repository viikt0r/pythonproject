from rest_framework import generics, mixins, permissions
from . models import Marque
from . serializers import MarquesSerializer, MarquesAllSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly
from django.core.files.storage import FileSystemStorage

class MarqueListView(mixins.CreateModelMixin, generics.ListAPIView):
    id = 'pk'
    serializer_class = MarquesSerializer

    def get_queryset(self):
        qs = Marque.objects.all()
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


class MarqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = MarquesSerializer

    def get_queryset(self):
        return Marque.objects.all()


class MarqueDeal(generics.ListAPIView):
    id = 'pk'
    serializer_class = MarquesAllSerializer

    def get_queryset(self):
        return Marque.objects.all()