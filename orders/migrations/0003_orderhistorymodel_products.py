# Generated by Django 4.0.6 on 2022-09-20 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0002_orderhistorymodel_delete_shophistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistorymodel',
            name='products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.productmodel'),
            preserve_default=False,
        ),
    ]