# Generated by Django 4.2.3 on 2023-07-25 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiku', '0005_alter_option_opt_alter_scoreinterval_max_score_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name_plural': '答题卡选项'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name_plural': '测试试卷题目'},
        ),
        migrations.AlterModelTableComment(
            name='option',
            table_comment='答题卡选项',
        ),
        migrations.AlterModelTableComment(
            name='subject',
            table_comment='测试试卷题目',
        ),
    ]