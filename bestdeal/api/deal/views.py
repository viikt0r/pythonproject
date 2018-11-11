from rest_framework import generics, mixins
from . models import Deal
from . serializers import DealsAllSerializer, DealsSerializer
from django.db.models import Q


class DealListView(mixins.CreateModelMixin, generics.ListAPIView):
    id = 'pk'
    serializer_class = DealsAllSerializer

    def get_queryset(self):
        qs = Deal.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(dea_title=query) | Q(dea_contenu=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    id = 'pk'
    serializer_class = DealsAllSerializer

    def get_queryset(self):
        return Deal.objects.all()


class DealNoFk(generics.ListAPIView):
    id = 'pk'
    queryset = Deal.objects.all()
    serializer_class = DealsSerializer
