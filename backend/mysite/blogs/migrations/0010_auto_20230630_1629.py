# Generated by Django 3.2 on 2023-06-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0009_auto_20230626_0238"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="CHcontent",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="ENcontent",
            field=models.TextField(blank=True),
        ),
    ]
