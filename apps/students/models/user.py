from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)

