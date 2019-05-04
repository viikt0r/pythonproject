from rest_framework import generics, mixins, permissions
from . models import Comment
from . serializers import CommentSerializer
from django.db.models import Q
from . . . permissions import IsOwnerOrReadOnly

class CommentListView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = Comment.objects.all()
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


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    id = 'pk'
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()