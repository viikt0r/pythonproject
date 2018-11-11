from django.contrib import admin
from bestdeal.api.deal.models import Deal
from bestdeal.api.marque.models import Marque
from bestdeal.api.tag.models import Tag
from bestdeal.api.commentaire.models import Comment

admin.site.register(Deal)
admin.site.register(Marque)
admin.site.register(Tag)
admin.site.register(Comment)
