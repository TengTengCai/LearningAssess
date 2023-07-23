from django.contrib import admin

from apps.config.models import CourseInfo, Config


class ConfigAdmin(admin.ModelAdmin):
    fields = ['index_image', 'xetong_address', 'shop_address', 'evaluation_image']
    list_display = ['id', 'index_image', 'xetong_address', 'shop_address', 'evaluation_image']
    list_display_links = ['id']

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    def get_actions(self, request):
        # 在actions中去掉‘删除’操作
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


# Register your models here.
class CourseInfoAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'image']
    list_display = ['id', 'title', 'url', 'image']
    list_display_links = ['id', 'title']


admin.site.register(Config, ConfigAdmin)
admin.site.register(CourseInfo, CourseInfoAdmin)
