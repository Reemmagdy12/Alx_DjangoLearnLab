from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth,profile_photo):
        if not date_of_birth :
            raise ValueError(('The date of birth must be defined'))
        user = self.model(
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )
        user.save(using=self._db)
        return user 
    def create_superuser(self,date_of_birth,profile_photo):
        user = self.create_user(
            date_of_birth = date_of_birth, 
            profile_photo = profile_photo
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user 
        

class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField

    REQUIRED_FIELDS =[date_of_birth]
    objects = CustomUserManager()

    def _str_(self):
        return self.date_of_birth
