# Generated by Django 4.0.6 on 2022-08-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_postmodel_image_2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='posts_2', verbose_name='image_2'),
        ),
    ]