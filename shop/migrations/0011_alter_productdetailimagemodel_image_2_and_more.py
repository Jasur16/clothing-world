# Generated by Django 4.0.6 on 2022-08-07 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_productmodel_detail_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetailimagemodel',
            name='image_2',
            field=models.ImageField(null=True, upload_to='detail_image', verbose_name='image_2'),
        ),
        migrations.AlterField(
            model_name='productdetailimagemodel',
            name='image_3',
            field=models.ImageField(null=True, upload_to='detail_image', verbose_name='image_3'),
        ),
    ]