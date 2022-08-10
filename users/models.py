from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator


class UserModel(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('first name'),
        validators=[MinLengthValidator(limit_value=4)]
    )
    last_name = models.CharField(max_length=50, verbose_name=_('last name'))
    username = models.CharField(max_length=50, unique=True, verbose_name=_('username'))
    password = models.CharField(max_length=16, verbose_name=_('password'))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
