from django.db import models
from django.core.files.storage import FileSystemStorage
import uuid

fs = FileSystemStorage(location='/photos_marques')

class Marque(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(storage=fs, default='')
    link = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_add = models.ForeignKey('auth.User', related_name='mar_users', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def test(self):
        return self.name + ' link : ' + self.link 
        
