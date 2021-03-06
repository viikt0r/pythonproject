from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from . . tag.models import Tag
from . . brand.models import Brand
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid
import os


def deal_image_file_path(instance, filename):
    """Generate file path for new deal image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/deal/', filename)


class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    link = models.URLField(default='')
    photo = models.ImageField(null=True, upload_to=deal_image_file_path)
    content = models.TextField(default='')
    promo_code = models.CharField(max_length=50, null=True, default='')
    statut_promo = models.BooleanField(default=False)
    price_before = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    price_after = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    in_shop = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    country = CountryField(blank_label='(select country)',
                           blank=True, null=True, default='CA')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand_fk = models.ForeignKey(
        Brand, related_name='dea_brands', on_delete=models.CASCADE, default='')
    tag_set = models.ManyToManyField(Tag, related_name='dea_tags')
    user_add = models.ForeignKey(
        User, related_name='dea_users', on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']

    def __str__(self):
        return self.title


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    sco_dea_fk = models.ForeignKey(
        Deal, related_name='sco_deals', on_delete=models.CASCADE)
    user_add = models.ForeignKey(
        User, related_name='sco_users', on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(-1), MinValueValidator(1), ])  # -1 ou 1
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.score


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    id_guid = models.UUIDField(default=uuid.uuid4, editable=False)
    fol_dea_fk = models.ForeignKey(
        Deal, on_delete=models.CASCADE, related_name='follow_deals')
    user_follow = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follow_users')
    created_at = models.DateTimeField(auto_now_add=True)
