from django.contrib import admin

from .models import TestPaper, LargeClass, SubClass, ScoreInterval, Subject


# Register your models here.


class TestPaperAdmin(admin.ModelAdmin):
    fields = ['paper_name', 'description']
    list_display = ['id', 'paper_name', 'description']
    list_display_links = ['id', 'paper_name', 'description']


class LargeClassAdmin(admin.ModelAdmin):
    fields = ['test_paper', 'class_name', 'description']
    list_display = ['id', 'test_paper', 'class_name', 'description']
    list_display_links = ['id', 'class_name', 'description']


class SubClassAdmin(admin.ModelAdmin):
    fields = ['large_class', 'class_name', 'description']
    list_display = ['id', 'large_class', 'class_name', 'description']
    list_display_links = ['id', 'class_name', 'description']


class ScoreIntervalAdmin(admin.ModelAdmin):
    fields = ['sub_class', 'min_score', 'max_score', 'description']
    list_display = ['id', 'sub_class', 'min_score', 'max_score', 'description']
    list_display_links = ['id', 'sub_class']


class SubjectAdmin(admin.ModelAdmin):
    fields = [
        'test_paper', 'large_class', 'sub_class', 'topic', 'a_ans', 'a_score',
        'b_ans', 'b_score', 'c_ans', 'c_score', 'd_ans', 'd_score', 'e_ans', 'e_score']
    list_display = ['id', 'test_paper', 'large_class', 'sub_class', 'topic']
    list_display_links = ['id', 'topic']


admin.site.register(TestPaper, TestPaperAdmin)
admin.site.register(LargeClass, LargeClassAdmin)
admin.site.register(SubClass, SubClassAdmin)
admin.site.register(ScoreInterval, ScoreIntervalAdmin)
admin.site.register(Subject, SubjectAdmin)
