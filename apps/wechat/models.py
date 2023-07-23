from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import BaseModel


class User(BaseModel):
    class SexSelect(models.TextChoices):
        NAN = "0", _("男")
        NV = "1", _("女")

    openid = models.CharField(max_length=128, unique=True, help_text='小程序中的openid')
    name = models.CharField(verbose_name='姓名', max_length=16, help_text='用户姓名')
    sex = models.CharField(verbose_name='性别', max_length=2, choices=SexSelect.choices)
    age = models.IntegerField(verbose_name='年龄', help_text='用户年龄')
    grade = models.CharField(verbose_name='年级', max_length=32, help_text='用户年龄')
    phone = models.CharField(verbose_name='手机号', unique=True, max_length=11, help_text='用户手机号')
    group_number = models.CharField(
        verbose_name='群号', max_length=128, default='', null=True, blank=True,
        help_text='你所在群的群号（1群请填1，以此类推）')

    def __str__(self):
        return f"{self.name}_{self.phone}"

    class Meta:
        verbose_name_plural = '高考用户'
        db_table_comment = "高考用户"
