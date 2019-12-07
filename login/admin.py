from django.contrib import admin
from . import models
# Register your models here.

# 修改后台管理界面
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_id', 'major', 'college', 'degree', 'grade', 'gender', 'native_place', 'email', 'phone', 'c_time']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'college', 'degree', 'grade', 'gender', 'c_time']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Student, StudentAdmin)
