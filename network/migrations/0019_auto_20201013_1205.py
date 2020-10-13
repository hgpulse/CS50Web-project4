# Generated by Django 3.1.2 on 2020-10-13 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_auto_20201013_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='network.profile'),
        ),
    ]
