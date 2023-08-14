from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# # Create your models here.
# class Users(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.CharField(max_length=100, null=True, blank=True)
#     password = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
class UserProfile(AbstractUser):
    '''
    User System
    '''
    groups = models.ManyToManyField(Group, blank=True,
                                    related_name='userprofile_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True,
                                              related_name='userprofile_user_permissions')
    LEVEL = (
        (1, 'User'),
        (2, 'Admin'),
    )
    name = models.CharField(max_length=100, null=True, blank=True,
                            verbose_name='Name')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email')
    level = models.IntegerField(choices=LEVEL, default=1, verbose_name='Level')
