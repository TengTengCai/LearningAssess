import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


def image_upload_to(instance, filename):
    return '{class_name}/{uuid}/{filename}'.format(
        class_name=instance.__class__.__name__, uuid=uuid.uuid4().hex, filename=filename)


class Config(BaseModel):
    index_image = models.ImageField(
        verbose_name='首页大图', default='', null=True, blank=True, help_text='首页顶部大图',
        upload_to=image_upload_to)
    xetong_address = models.URLField(
        verbose_name='树成林公众号地址', default='', null=True, blank=True, help_text='首页左侧公众号地址')
    shop_address = models.URLField(
        verbose_name='逆袭商店地址', default='', null=True, blank=True, help_text='首页右侧商店地址')
    evaluation_image = models.ImageField(
        verbose_name='学习力测评图', default='', null=True, blank=True, help_text='中间部分的学习力测评图',
        upload_to=image_upload_to)

    class Meta:
        verbose_name_plural = "全局配置"
        db_table_comment = "全局配置"


class CourseInfo(BaseModel):
    title = models.CharField(max_length=256, verbose_name='标题', help_text='标题')
    url = models.URLField(verbose_name='链接', help_text='点击的相关链接')
    image = models.ImageField(verbose_name='图片地址', help_text='图片地址', upload_to=image_upload_to)

    class Meta:
        verbose_name_plural = "课程资讯"
        db_table_comment = "课程资讯"


class Article(BaseModel):
    class ArticleType(models.TextChoices):
        CUR = "curation", _("精选")
        HIS = "history", _("历史")
        COM = "community", _("社区推荐")
    title = models.CharField(max_length=256, verbose_name='标题', help_text='标题')
    a_type = models.CharField(
        max_length=16, choices=ArticleType.choices, verbose_name='类型', help_text='类型')
    description = models.TextField(verbose_name='描述', help_text='描述')
    image = models.ImageField(verbose_name='文章图片地址', help_text='文章图片地址', upload_to=image_upload_to)
    url = models.URLField(verbose_name='链接', help_text='文章点击的相关链接')

    class Meta:
        verbose_name_plural = "文章管理"
        db_table_comment = "文章管理"
