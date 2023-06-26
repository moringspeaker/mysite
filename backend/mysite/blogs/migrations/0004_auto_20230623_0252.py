# Generated by Django 3.2 on 2023-06-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20230623_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='belong_to_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='collection',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]