# Generated by Django 3.0.1 on 2020-01-05 21:35

import apis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20200105_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=apis.models.get_profile_photo_path),
        ),
    ]