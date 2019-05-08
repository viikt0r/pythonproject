# Generated by Django 2.2.1 on 2019-05-08 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestdeal', '0003_auto_20190506_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbuseReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('url_deal', models.URLField(default='')),
                ('text', models.TextField()),
                ('spam', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('abu_com_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abuse_comment', to='bestdeal.Comment')),
                ('abu_dea_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abuse_deal', to='bestdeal.Deal')),
                ('user_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abuse_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
