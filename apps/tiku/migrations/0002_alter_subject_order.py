# Generated by Django 4.2.3 on 2023-07-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='order',
            field=models.IntegerField(default=0, help_text='题目序号', verbose_name='序号'),
        ),
    ]