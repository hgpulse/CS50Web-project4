# Generated by Django 3.1.2 on 2020-10-13 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0020_remove_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
