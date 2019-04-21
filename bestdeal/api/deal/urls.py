from django.urls import re_path
from . views import DealListView, DealDetailView, DealNoFk, DealCommentDetailView, ScoreListView


urlpatterns = [
    re_path(r'^deals/$', DealListView.as_view(), name='deal-list'),
    re_path(r'^deals/(?P<pk>[0-9a-f-]+)/$', DealDetailView.as_view(), name='deal-detail'),
    re_path(r'^deals/(?P<pk>[0-9a-f-]+)/comment/$', DealCommentDetailView.as_view(), name='deal-comment-detail'),
    re_path(r'^scores/$', ScoreListView.as_view(), name='score-list'),
    re_path(r'^deals/nofk/$', DealNoFk.as_view(), name='deal-list-all'),
]
