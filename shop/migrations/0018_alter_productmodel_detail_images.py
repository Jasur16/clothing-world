# Generated by Django 4.0.6 on 2022-08-13 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_productmodel_real_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='detail_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.productdetailimagemodel', verbose_name='detail images'),
        ),
    ]
