from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('nmae'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class MenBannerModel(models.Model):
    collections = models.CharField(max_length=100, verbose_name=_('collections'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='men_banner')
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'men_banner'
        verbose_name_plural = 'men_banners'


class WomenBannerModel(models.Model):
    collections = models.CharField(max_length=100, verbose_name=_('collections'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='men_banner')
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'women_banner'
        verbose_name_plural = 'women_banners'
