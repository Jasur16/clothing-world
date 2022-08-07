# Generated by Django 4.0.6 on 2022-08-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_colormodel_sizemodel_productmodel_colors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetailImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='detail_image', verbose_name='image_1')),
                ('image_2', models.ImageField(upload_to='detail_image', verbose_name='image_2')),
                ('image_3', models.ImageField(upload_to='detail_image', verbose_name='image_3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'detail_image',
                'verbose_name_plural': 'detail_images',
            },
        ),
    ]
