from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)

