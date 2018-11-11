from django.db import models
from bestdeal.api.deal.models import Deal
from django.contrib.auth.models import User
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)
    com_dea_fk = models.ForeignKey(Deal, related_name='com_deals', on_delete=models.CASCADE)
    user_add = models.ForeignKey(User, related_name='com_users', on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
