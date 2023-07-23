from django.contrib import admin

from apps.wechat.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['openid', 'name', 'sex', 'age', 'grade', 'phone',
              'group_number']
    list_display = ['id', 'name', 'openid', 'sex', 'age', 'grade', 'phone',
                    'group_number']
    list_display_links = ['id', 'name']


admin.site.register(User, UserAdmin)
