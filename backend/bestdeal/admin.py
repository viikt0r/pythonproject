from django.contrib import admin
from . api.deal.models import Deal
from . api.brand.models import Brand
from . api.tag.models import Tag
from . api.commentaire.models import Comment
from . api.abuse_report.models import AbuseReport

admin.site.register(Deal)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(AbuseReport)
