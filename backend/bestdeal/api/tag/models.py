from django.db import models
from django.contrib.auth.models import User
import uuid, os


def tag_image_file_path(instance, filename):
    """Generate file path for new tag image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/tag/', filename)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, upload_to=tag_image_file_path)
    main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey(User, related_name='tag_users', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
