# Generated by Django 4.0.6 on 2022-08-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_barcategorymodel_name_en_barcategorymodel_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetailimagemodel',
            name='image_1',
            field=models.ImageField(null=True, upload_to='detail_image', verbose_name='image_1'),
        ),
    ]
