# Generated by Django 4.0.6 on 2022-08-07 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_productdetailimagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='detail_images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.productdetailimagemodel', verbose_name='detail images'),
        ),
    ]
