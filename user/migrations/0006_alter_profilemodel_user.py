# Generated by Django 4.0.6 on 2022-09-19 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profilemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
