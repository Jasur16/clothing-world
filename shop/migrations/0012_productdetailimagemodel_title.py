# Generated by Django 4.0.6 on 2022-08-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_productdetailimagemodel_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetailimagemodel',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]