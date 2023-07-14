from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=140, default='SOME STRING')

    def __str__(self):
        return self.name
