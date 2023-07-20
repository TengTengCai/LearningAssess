from django.db import models

from utils.base_model import BaseModel


# Create your models here.
class TestPaper(BaseModel):
    paper_name = models.CharField(verbose_name='测试名称', max_length=128, help_text='测试名称')
    description = models.TextField(verbose_name='说明', null=True, blank=True, help_text='说明')

    class Meta:
        verbose_name_plural = '测试试卷'
        db_table_comment = "测试试卷"


class LargeClass(BaseModel):
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, help_text='测试试卷')
    class_name = models.CharField(max_length=64, help_text='大类名称')
    description = models.TextField(help_text='说明', null=True, blank=True)

    class Meta:
        db_table_comment = "大类目"


class SubClass(BaseModel):
    class_name = models.CharField(max_length=64, help_text='小类名称')
    large_class = models.ForeignKey(LargeClass, on_delete=models.CASCADE, help_text='大类目')
    description = models.TextField(help_text='说明', null=True, blank=True)

    class Meta:
        db_table_comment = "小类目"


class ScoreInterval(BaseModel):
    sub_class = models.ForeignKey(SubClass, on_delete=models.CASCADE, help_text='小类目')
    min_score = models.IntegerField(help_text='最小值', default=0)
    max_score = models.IntegerField(help_text='最大值', default=100)
    description = models.TextField(help_text='说明', null=True, blank=True)

    class Meta:
        db_table_comment = "分数区间"


class Subject(BaseModel):
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, help_text='测试试卷')
    large_class = models.ForeignKey(LargeClass, on_delete=models.CASCADE, help_text='大类目')
    sub_class = models.ForeignKey(SubClass, on_delete=models.CASCADE, help_text='小类目')
    topic = models.TextField(help_text='题目')
    a_ans = models.CharField(max_length=128, default='A.根本不是这样', help_text='A选项')
    a_score = models.IntegerField(default=1)
    b_ans = models.CharField(max_length=128, default='B.这不太像我', help_text='B选项')
    b_score = models.IntegerField(default=2)
    c_ans = models.CharField(max_length=128, default='C.我不好说', help_text='C选项')
    c_score = models.IntegerField(default=3)
    d_ans = models.CharField(max_length=128, default='D.这比较像我', help_text='D选项')
    d_score = models.IntegerField(default=4)
    e_ans = models.CharField(max_length=128, default='E.我就是这样', help_text='E选项')
    e_score = models.IntegerField(default=5)

    class Meta:
        db_table_comment = "题目"
