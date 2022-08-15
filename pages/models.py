from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from config.validators import PhoneValidator


class ContactModel(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name=_('name'),
        validators=[
            MinLengthValidator(limit_value=4),
            MaxLengthValidator(limit_value=30)
        ])
    email = models.EmailField(verbose_name=_('email'), validators=[EmailValidator()])
    phone = models.CharField(max_length=13, verbose_name=_('phone'), null=True, validators=[PhoneValidator()])
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


class AboutModel(models.Model):
    our_story = RichTextUploadingField(verbose_name=_('our story'))
    our_story_image = models.ImageField(upload_to='about_img', verbose_name=_('our store image'))
    our_mission = RichTextUploadingField(verbose_name=_('our mission'))
    our_mission_image = models.ImageField(upload_to='about_img', verbose_name=_('our mission image'), null=True)
    banner_image = models.ImageField(upload_to='about_img', verbose_name=_('banner image'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.our_story}{self.our_mission}"

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'
