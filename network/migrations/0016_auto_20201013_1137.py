# Generated by Django 3.1.2 on 2020-10-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20201013_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
        migrations.AddField(
            model_name='profile',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, to='network.Post'),
        ),
    ]
