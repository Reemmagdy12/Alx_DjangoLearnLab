from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    bio = models.TextField
    followers = models.ManyToManyField('self',symmetrical=False,related_name='following')
    profile_picture = models.ImageField

def __str__(self):
    return self.username
