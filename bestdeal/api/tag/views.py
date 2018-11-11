from rest_framework import generics, mixins
from . models import Tag
from . serializers import TagSerializer
from django.db.models import Q


class TagListView(mixins.CreateModelMixin, generics.ListAPIView):
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
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    id = 'pk'
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()

