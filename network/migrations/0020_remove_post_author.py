# Generated by Django 3.1.2 on 2020-10-13 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_auto_20201013_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
