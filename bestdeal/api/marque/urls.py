from django.urls import re_path
from . views import MarqueListView, MarqueDetailView, MarqueFk

urlpatterns = [
    re_path(r'^marques/$', MarqueListView.as_view(), name='marque-list-nofk'),
    re_path(r'^marques/(?P<pk>[0-9a-f-]+)/$', MarqueDetailView.as_view(), name='marque_detail'),
    re_path(r'^marques/fk/$', MarqueFk.as_view(), name='marque-list-fk'),
]
