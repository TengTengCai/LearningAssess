# Generated by Django 4.2.3 on 2023-08-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiku', '0011_alter_surveyresult_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='largeclass',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='subclass',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='testpaper',
            name='total_score',
        ),
    ]
