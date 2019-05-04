from django.urls import re_path
from . views import CommentListView, CommentDetailView


urlpatterns = [
    re_path(r'^comments/$', CommentListView.as_view(), name='comment-list'),
    re_path(r'^comments/(?P<pk>[0-9a-f-]+)/$', CommentDetailView.as_view(), name='comment-detail'),
]
