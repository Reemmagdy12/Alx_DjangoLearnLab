from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    bio = models.TextField
    followers = models.ManyToManyField(AbstractUser)
    profile_picture = models.ImageField
