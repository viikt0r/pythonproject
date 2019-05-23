from django.urls import re_path
from . views import MarqueListView, MarqueDetailView, MarqueListDeal

urlpatterns = [
    # sans les deals
    re_path(r'^marques/$', MarqueListView.as_view(), name='marque-list-nofk'),
    re_path(r'^marques/(?P<pk>[0-9a-f-]+)/$', MarqueDetailView.as_view(), name='marque-detail'),
    # avec les deals
    re_path(r'^marques/deals/$', MarqueListDeal.as_view(), name='marque-list-deal'),
]
