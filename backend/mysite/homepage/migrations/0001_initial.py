# Generated by Django 3.2 on 2023-06-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ENtitle', models.CharField(blank=True, max_length=200)),
                ('CHtitle', models.CharField(blank=True, max_length=200)),
                ('src', models.ImageField(default='static/no-img.jpg', upload_to='medias/swipers/')),
            ],
        ),
    ]
