# Generated by Django 3.1.2 on 2020-10-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20201009_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(),
        ),
    ]
