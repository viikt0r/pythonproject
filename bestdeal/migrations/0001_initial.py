# Generated by Django 2.1.3 on 2018-11-04 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(default='')),
                ('content', models.TextField(default='')),
                ('price_before', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('price_after', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('shipping', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('start_date', models.DateField(default=None)),
                ('end_date', models.DateField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mar_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sco_dea_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sco_deals', to='bestdeal.Deal')),
                ('user_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sco_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='dea_mar_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dea_marques', to='bestdeal.Marque'),
        ),
        migrations.AddField(
            model_name='deal',
            name='tag_set',
            field=models.ManyToManyField(to='bestdeal.Tag'),
        ),
        migrations.AddField(
            model_name='deal',
            name='user_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dea_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='com_dea_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_deals', to='bestdeal.Deal'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_users', to=settings.AUTH_USER_MODEL),
        ),
    ]