from rest_framework import generics
from . models import Comment
from . serializers import CommentSerializer


class CommentListView(generics.ListAPIView):
    id = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
