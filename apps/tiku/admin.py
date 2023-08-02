from django.contrib import admin
from django.http import HttpResponse
from openpyxl.workbook import Workbook

from .models import TestPaper, LargeClass, SubClass, TotalScoreInterval, LargeScoreInterval, SubScoreInterval, \
    Subject, SurveyResult, Option


# Register your models here.
class SubjectInline(admin.TabularInline):
    model = Subject
    raw_id_fields = ['test_paper']


class OptionInline(admin.TabularInline):
    model = Option
    raw_id_fields = ['servey_result']


class TestPaperAdmin(admin.ModelAdmin):
    fields = ['paper_name', 'total_score', 'spend_time', 'description']
    list_display = ['id', 'paper_name', 'total_score', 'spend_time', 'description']
    list_display_links = ['id', 'paper_name', 'total_score', 'spend_time', 'description']
    inlines = [
      SubjectInline
    ]


class LargeClassAdmin(admin.ModelAdmin):
    fields = ['test_paper', 'class_name', 'total_score', 'description']
    list_display = ['id', 'test_paper', 'class_name', 'total_score', 'description']
    list_display_links = ['id', 'class_name', 'total_score', 'description']


class SubClassAdmin(admin.ModelAdmin):
    fields = ['large_class', 'class_name', 'total_score', 'description']
    list_display = ['id', 'large_class', 'class_name', 'total_score', 'description']
    list_display_links = ['id', 'class_name', 'total_score', 'description']


class TotalScoreIntervalAdmin(admin.ModelAdmin):
    fields = ['test_paper', 'min_score', 'max_score', 'grade', 'description']
    list_display = ['id', 'test_paper', 'min_score', 'max_score', 'grade', 'description']
    list_display_links = ['id', 'test_paper']


class LargeScoreIntervalAdmin(admin.ModelAdmin):
    fields = ['large_class', 'min_score', 'max_score', 'grade', 'description']
    list_display = ['id', 'large_class', 'min_score', 'max_score', 'grade', 'description']
    list_display_links = ['id', 'large_class']


class SubScoreIntervalAdmin(admin.ModelAdmin):
    fields = ['sub_class', 'min_score', 'max_score', 'grade', 'description']
    list_display = ['id', 'sub_class', 'min_score', 'max_score', 'description']
    list_display_links = ['id', 'sub_class']


class SubjectAdmin(admin.ModelAdmin):
    fields = [
        'test_paper', 'large_class', 'sub_class', 'order', 'topic', 'a_ans', 'a_score',
        'b_ans', 'b_score', 'c_ans', 'c_score', 'd_ans', 'd_score', 'e_ans', 'e_score']
    list_display = ['id', 'test_paper', 'large_class', 'sub_class', 'topic']
    list_display_links = ['id', 'topic']


class SurveyResultAdmin(admin.ModelAdmin):
    fields = ['test_paper', 'user', 'openid', 'phone', 'college_score', 'school_level', 'completed']
    list_display = ['id', 'test_paper', 'user', 'openid', 'phone', 'college_score', 'school_level', 'completed']
    list_display_links = ['id', 'test_paper', 'user']
    list_filter = ('completed',)
    inlines = [
      OptionInline
    ]

    # def export_survey_result_excel(self, request, queryset):
    #     meta = self.model._meta  # 用于定义文件名, 格式为: app名.模型类名
    #     field_names = [field.name for field in meta.fields]  # 模型所有字段名
    #
    #     response = HttpResponse(content_type='application/msexcel')  # 定义响应内容类型
    #     response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'  # 定义响应数据格式
    #     wb = Workbook()  # 新建Workbook
    #     ws = wb.active  # 使用当前活动的Sheet表
    #     ws.append(field_names)  # 将模型字段名作为标题写入第一行
    #     for obj in queryset:  # 遍历选择的对象列表
    #         for field in field_names:
    #             data = [f'{getattr(obj, field)}' for field in field_names]  # 将模型属性值的文本格式组成列表
    #         row = ws.append(data)  # 写入模型属性值
    #     wb.save(response)  # 将数据存入响应内容
    #     return response
    #     pass
    # actions = [export_survey_result_excel]


class OptionAdmin(admin.ModelAdmin):
    fields = ['servey_result', 'subject', 'opt', 'opt_score']
    list_display = ['id', 'servey_result', 'subject', 'opt', 'opt_score']
    list_display_links = ['id']


admin.site.register(TestPaper, TestPaperAdmin)
admin.site.register(LargeClass, LargeClassAdmin)
admin.site.register(SubClass, SubClassAdmin)
admin.site.register(TotalScoreInterval, TotalScoreIntervalAdmin)
admin.site.register(LargeScoreInterval, LargeScoreIntervalAdmin)
admin.site.register(SubScoreInterval, SubScoreIntervalAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SurveyResult, SurveyResultAdmin)
admin.site.register(Option, OptionAdmin)
