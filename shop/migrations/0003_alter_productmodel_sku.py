# Generated by Django 4.0.6 on 2022-08-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_categorymodel_name_alter_producttagmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='sku',
            field=models.CharField(max_length=50, unique=True, verbose_name='sku'),
        ),
    ]