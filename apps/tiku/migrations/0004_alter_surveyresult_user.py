# Generated by Django 4.2.3 on 2023-07-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_remove_user_college_score_remove_user_school_level'),
        ('tiku', '0003_surveyresult_college_score_surveyresult_results_json_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresult',
            name='user',
            field=models.ForeignKey(blank=True, help_text='用户', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wechat.user', verbose_name='用户'),
        ),
    ]
