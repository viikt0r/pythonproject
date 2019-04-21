from django.contrib import admin
from . api.deal.models import Deal
from . api.marque.models import Marque
from . api.tag.models import Tag
from . api.commentaire.models import Comment

admin.site.register(Deal)
admin.site.register(Marque)
admin.site.register(Tag)
admin.site.register(Comment)
