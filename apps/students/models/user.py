from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices
from apps.teachers.models.teachers import BaseModel

class User(AbstractUser, BaseModel):
    class UserType(TextChoices):
        STUDENT = 'STUDENT'
        TEACHER = 'TEACHER'
        ADMIN = 'ADMIN'
    image = models.ImageField(upload_to='users/images/%Y/%m/%d', blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.STUDENT)

