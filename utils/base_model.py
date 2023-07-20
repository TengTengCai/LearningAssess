from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    updated = models.DateTimeField(auto_now=True, help_text='更新时间')
    delete = models.BooleanField(default=False, help_text='假删除标志')

    class Meta:
        abstract = True
