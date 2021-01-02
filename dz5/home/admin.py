from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib import admin

from home.models import Student


class StudentAdmin(ModelAdmin):

    list_display = ("name", "email", "birthday")


admin.site.register(Student, StudentAdmin)