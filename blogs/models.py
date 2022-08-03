from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class AutherModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('full name'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('auther')
        verbose_name_plural = _('authers')


class PostTagModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('tag'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = RichTextUploadingField(verbose_name=_('body'))
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    auther = models.ForeignKey(AutherModel, related_name='posts', on_delete=models.RESTRICT)
    tag = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tag'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title[:100]

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    comment = models.TextField(verbose_name=_('comment'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return f"{self.comment}\n{self.name}\n{self.email}\n{self.phone}"

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
