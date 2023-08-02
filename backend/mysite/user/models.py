from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name