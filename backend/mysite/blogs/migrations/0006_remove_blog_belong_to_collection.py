# Generated by Django 3.2 on 2023-06-23 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20230623_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='belong_to_collection',
        ),
    ]