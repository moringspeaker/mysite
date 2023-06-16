
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Swiper(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='medias/swipers/', default='static/no-img.jpg')
    def __str__(self):
        return self.title
