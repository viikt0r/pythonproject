from rest_framework import generics, mixins
from . models import Marque
from . serializers import MarquesSerializer, MarquesAllSerializer
from django.db.models import Q


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
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MarqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    id = 'pk'
    serializer_class = MarquesSerializer

    def get_queryset(self):
        return Marque.objects.all()


class MarqueFk(generics.ListAPIView):
    id = 'pk'
    queryset = Marque.objects.all()
    serializer_class = MarquesAllSerializer