from django.urls import re_path
from bestdeal.api.commentaire.views import CommentListView


urlpatterns = [
    re_path(r'^comments/$', CommentListView.as_view(), name='comment-list'),
]
