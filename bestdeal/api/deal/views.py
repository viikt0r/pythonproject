from rest_framework import generics, mixins, permissions
from . models import Deal, Score
from . serializers import DealsAllSerializer, DealsSerializer, DealsCommentSerializer, ScoreSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly


class DealListView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
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
        serializer.save(user_add=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = DealsAllSerializer

    def get_queryset(self):
        return Deal.objects.all()


class DealNoFk(generics.ListAPIView):
    id = 'pk'
    queryset = Deal.objects.all()
    serializer_class = DealsSerializer

class DealCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
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

#from django.db.models import Sum
#all_sum = transaction.aggregate(Sum('amount'))['amount__sum']
#return Response({'sum': all_sum if all_sum else 0 , 'objects': serializer.data})
