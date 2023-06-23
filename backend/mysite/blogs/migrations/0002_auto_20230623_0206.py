# Generated by Django 3.2 on 2023-06-23 06:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('ENtitle', models.CharField(blank=True, max_length=200)),
                ('ENsummary', models.CharField(default='"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."', max_length=200)),
                ('CHtitle', models.CharField(blank=True, max_length=200)),
                ('CHsummary', models.CharField(default='惟柔弱是爱愿的识别，正如放弃是喧嚣的解剂', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='collection',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='blogs.collection', to_field='name'),
        ),
    ]
