
# Create your models here.
from django.db import models


class Swiper(models.Model):
    id = models.AutoField(primary_key=True)
    ENtitle = models.CharField(max_length=200,blank=True)
    CHtitle = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to='medias/swipers/', default='static/no-img.jpg')
    def __str__(self):
        return self.ENtitle
