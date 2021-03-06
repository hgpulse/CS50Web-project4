# Generated by Django 3.1.2 on 2020-10-13 09:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_profile_followed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Followed_by',
            field=models.ManyToManyField(blank=True, related_name='Followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='post',
            field=models.ManyToManyField(blank=True, to='network.Post'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
