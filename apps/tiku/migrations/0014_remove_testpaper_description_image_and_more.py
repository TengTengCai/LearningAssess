# Generated by Django 4.2.3 on 2023-08-14 16:28

import apps.tiku.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiku', '0013_testpaper_description_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpaper',
            name='description_image',
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='description',
            field=models.ImageField(blank=True, default='', help_text='说明图片', null=True, upload_to=apps.tiku.models.image_upload_to, verbose_name='说明图片'),
        ),
    ]
