# Generated by Django 4.2.3 on 2023-08-13 16:14

import apps.tiku.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiku', '0012_remove_largeclass_total_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpaper',
            name='description_image',
            field=models.ImageField(blank=True, default='', help_text='说明图片', null=True, upload_to=apps.tiku.models.image_upload_to, verbose_name='说明图片'),
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='spend_time',
            field=models.IntegerField(blank=True, default=12, null=True, verbose_name='预计花费时间(min)'),
        ),
    ]
