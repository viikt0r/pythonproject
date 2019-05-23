from django.db import models
from . . deal.models import Deal
from . . commentaire.models import Comment
from django.contrib.auth.models import User
import uuid


class AbuseReport(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    url_deal = models.URLField(default='')
    text = models.TextField()
    spam = models.BooleanField(default=False)
    abu_dea_fk = models.ForeignKey(Deal, related_name='abuse_deal', on_delete=models.CASCADE, blank=True, null=True,)
    abu_com_fk = models.ForeignKey(Comment, related_name='abuse_comment', on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    user_add = models.ForeignKey(User, related_name='abuse_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.id