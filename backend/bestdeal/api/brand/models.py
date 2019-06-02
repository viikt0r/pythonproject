from django.db import models
import uuid, os

def brand_image_file_path(instance, filename):
    """Generate file path for new brand image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/brand/', filename)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, upload_to=brand_image_file_path)
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
        
