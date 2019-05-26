from django.db import models
from bestdeal.api.deal.models import Deal
from django.contrib.auth.models import User
import uuid


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    text = models.TextField()
    approved_comment = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    com_dea_fk = models.ForeignKey(Deal, related_name='com_deals', on_delete=models.CASCADE)
    user_add = models.ForeignKey(User, related_name='com_users', on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    lik_com_fk = models.ForeignKey(Comment, related_name='lik_comments', on_delete=models.CASCADE)
    user_add = models.ForeignKey(User, related_name='lik_comments', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.like
