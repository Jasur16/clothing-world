# Generated by Django 4.0.6 on 2022-08-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_menbannermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenBannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collections', models.CharField(max_length=100, verbose_name='collections')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(upload_to='men_banner')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'women_banner',
                'verbose_name_plural': 'women_banners',
            },
        ),
    ]