from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.wechat.models import User
from utils.base_model import BaseModel


# Create your models here.
class TestPaper(BaseModel):
    paper_name = models.CharField(verbose_name='测试名称', max_length=128, help_text='测试名称')
    description = models.TextField(verbose_name='说明', null=True, blank=True, help_text='说明')

    def __str__(self):
        return self.paper_name

    class Meta:
        verbose_name_plural = '测试试卷'
        db_table_comment = "测试试卷"


class LargeClass(BaseModel):
    test_paper = models.ForeignKey(
        TestPaper, verbose_name='测试试卷',  on_delete=models.CASCADE, help_text='测试试卷')
    class_name = models.CharField(verbose_name='大类名称', max_length=64, help_text='大类名称')
    description = models.TextField(verbose_name='说明', help_text='说明', null=True, blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = '大类目'
        db_table_comment = "大类目"


class SubClass(BaseModel):
    large_class = models.ForeignKey(
        LargeClass, verbose_name='大类目', on_delete=models.CASCADE, help_text='大类目')
    class_name = models.CharField(verbose_name='小类名称', max_length=64, help_text='小类名称')
    description = models.TextField(verbose_name='说明', help_text='说明', null=True, blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = '小类目'
        db_table_comment = "小类目"


class ScoreInterval(BaseModel):
    sub_class = models.ForeignKey(SubClass, verbose_name='小类目', on_delete=models.CASCADE, help_text='小类目')
    min_score = models.IntegerField(verbose_name='最小值分数', help_text='最小值', default=0)
    max_score = models.IntegerField(verbose_name='最大值分数', help_text='最大值', default=100)
    description = models.TextField(verbose_name='说明', help_text='说明', null=True, blank=True)

    class Meta:
        verbose_name_plural = '小类分数区间'
        db_table_comment = "分数区间"


class Subject(BaseModel):
    test_paper = models.ForeignKey(
        TestPaper, verbose_name='测试试卷', on_delete=models.CASCADE, help_text='测试试卷')
    large_class = models.ForeignKey(
        LargeClass, verbose_name='所属大类', on_delete=models.CASCADE, help_text='大类目')
    sub_class = models.ForeignKey(
        SubClass, verbose_name='所属小类', on_delete=models.CASCADE, help_text='小类目')
    order = models.IntegerField(verbose_name='序号', default=0, help_text='题目序号')
    topic = models.TextField(verbose_name='题目', help_text='题目')
    a_ans = models.CharField(verbose_name='A选项', max_length=128, default='A.根本不是这样', help_text='A选项')
    a_score = models.IntegerField(verbose_name='A选项分数', default=1, null=True, blank=True)
    b_ans = models.CharField(verbose_name='B选项', max_length=128, default='B.这不太像我', help_text='B选项')
    b_score = models.IntegerField(verbose_name='B选项分数', default=2, null=True, blank=True)
    c_ans = models.CharField(verbose_name='C选项', max_length=128, default='C.我不好说', help_text='C选项')
    c_score = models.IntegerField(verbose_name='C选项分数', default=3, null=True, blank=True)
    d_ans = models.CharField(verbose_name='D选项', max_length=128, default='D.这比较像我', help_text='D选项')
    d_score = models.IntegerField(verbose_name='D选项分数', default=4, null=True, blank=True)
    e_ans = models.CharField(verbose_name='E选项', max_length=128, default='E.我就是这样', help_text='E选项')
    e_score = models.IntegerField(verbose_name='E选项分数', default=5, null=True, blank=True)

    def __str__(self):
        return f'{self.order}-{self.topic}'

    class Meta:
        verbose_name_plural = '题目'
        db_table_comment = "题目"


class SurveyResult(BaseModel):
    test_paper = models.ForeignKey(TestPaper, verbose_name='测试试卷', on_delete=models.CASCADE, help_text='测试试卷')
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.DO_NOTHING, help_text='用户')
    openid = models.CharField(max_length=128, help_text='小程序中的openid')
    phone = models.CharField(verbose_name='手机号', max_length=11, help_text='用户手机号')
    completed = models.BooleanField(verbose_name='是否完成答题', default=False)

    def __str__(self):
        return f'{self.test_paper}-{self.user.name}'

    class Meta:
        verbose_name_plural = '答题卡'
        db_table_comment = "答题卡"


class Option(BaseModel):
    class OPT(models.TextChoices):
        A = "a_ans", _("A")
        B = "b_ans", _("B")
        C = "c_ans", _("C")
        D = "d_ans", _("D")
        E = "e_ans", _("E")
    servey_result = models.ForeignKey(SurveyResult, verbose_name='调查结果', on_delete=models.CASCADE, help_text='问卷ID')
    subject = models.ForeignKey(Subject, verbose_name='题目', on_delete=models.CASCADE, help_text='题目')
    opt = models.CharField(
        verbose_name='当前选项',
        max_length=8,
        choices=OPT.choices,
        null=True, blank=True
    )
    opt_score = models.IntegerField(verbose_name='选项分数', default=0, null=True, blank=True)

    class Meta:
        verbose_name_plural = '选项'
        db_table_comment = "用户选项"
