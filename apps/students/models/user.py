from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from apps.teachers.models import BaseModel


class UserType(models.TextChoices):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'


class User(AbstractUser, BaseModel):
    image = models.ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.STUDENT)

