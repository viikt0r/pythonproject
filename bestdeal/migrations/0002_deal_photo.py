# Generated by Django 2.1.3 on 2018-11-04 22:53

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestdeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='photo',
            field=models.ImageField(default='', storage=django.core.files.storage.FileSystemStorage(location='/photos'), upload_to=''),
        ),
    ]