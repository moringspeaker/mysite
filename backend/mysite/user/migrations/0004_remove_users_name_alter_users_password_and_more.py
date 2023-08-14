# Generated by Django 4.1.7 on 2023-07-31 23:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_rename_user_users_username_alter_users_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="users",
            name="name",
        ),
        migrations.AlterField(
            model_name="users",
            name="password",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="users",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]