# Generated by Django 3.1.2 on 2020-10-14 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0034_auto_20201014_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
