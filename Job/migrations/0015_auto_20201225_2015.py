# Generated by Django 3.1.3 on 2020-12-25 19:15

import Job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0014_auto_20201225_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='images',
            field=models.ImageField(upload_to=Job.models.image_upload),
        ),
    ]
