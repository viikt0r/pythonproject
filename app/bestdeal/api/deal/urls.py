from django.urls import re_path
from . views import DealListView, DealDetailView, DealNoFk, DealCommentDetailView, ScoreListView, TagDeals, UserDeals, UserFollowDeals, FollowListView

urlpatterns = [
    re_path(r'^deals/$', DealListView.as_view(), name='deal-list'),
    re_path(r'^deals/(?P<pk>[0-9a-f-]+)/$', DealDetailView.as_view(), name='deal-detail'),
    re_path(r'^deals/(?P<pk>[0-9a-f-]+)/comment/$', DealCommentDetailView.as_view(), name='deal-comment-detail'),
    re_path(r'^scores/$', ScoreListView.as_view(), name='score-list'),
    re_path(r'^deals/nofk/$', DealNoFk.as_view(), name='deal-list-all'),
    re_path(r'^tags/(?P<pk>[0-9a-f-]+)/deals/$', TagDeals.as_view(), name='tag-list-deal'),
    re_path(r'^users/(?P<pk>[0-9a-f-]+)/deals/$', UserDeals.as_view(), name='user-list-deal'),
    re_path(r'^users/(?P<pk>[0-9a-f-]+)/follow/$', UserFollowDeals.as_view(), name='user-follow-deal'),
    re_path(r'^follow/$', FollowListView.as_view(), name='follow-list'),
]
