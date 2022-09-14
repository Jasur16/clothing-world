from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
