from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib import admin

from home.models import Student


class StudentAdmin(ModelAdmin):

    list_display = ("name", "email", "birthday", "students_social")

    def students_social(self, object):
        social = object.url
        return social



admin.site.register(Student, StudentAdmin)