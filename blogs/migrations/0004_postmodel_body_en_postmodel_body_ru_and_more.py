# Generated by Django 4.0.6 on 2022-08-15 15:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_postmodel_options_alter_postmodel_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='body_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='body_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
