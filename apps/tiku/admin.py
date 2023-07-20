from django.contrib import admin

from .models import TestPaper

# Register your models here.


class TestPaperAdmin(admin.ModelAdmin):
    fields = ['paper_name', 'description']
    list_display = ['paper_name', 'description']
    list_display_links = ['paper_name', 'description']


admin.site.register(TestPaper, TestPaperAdmin)
