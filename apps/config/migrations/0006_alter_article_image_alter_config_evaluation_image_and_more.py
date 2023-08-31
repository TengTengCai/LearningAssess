# Generated by Django 4.2.3 on 2023-08-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_alter_config_shop_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.URLField(help_text='文章图片地址', verbose_name='文章图片地址'),
        ),
        migrations.AlterField(
            model_name='config',
            name='evaluation_image',
            field=models.URLField(blank=True, default='', help_text='中间部分的学习力测评图', null=True, verbose_name='学习力测评图'),
        ),
        migrations.AlterField(
            model_name='config',
            name='index_image',
            field=models.URLField(blank=True, default='', help_text='首页顶部大图', null=True, verbose_name='首页大图'),
        ),
        migrations.AlterField(
            model_name='config',
            name='shop_address',
            field=models.URLField(blank=True, default='', help_text='逆袭商店二维码图片地址', null=True, verbose_name='逆袭商店二维码图片地址'),
        ),
        migrations.AlterField(
            model_name='config',
            name='xetong_address',
            field=models.URLField(blank=True, default='', help_text='树成林公众号二维码图片地址', null=True, verbose_name='树成林公众号二维码图片地址'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='image',
            field=models.URLField(help_text='图片地址', verbose_name='图片地址'),
        ),
    ]
