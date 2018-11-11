from django.db import models
from django.contrib.auth.models import User
import uuid


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, related_name='tag_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
