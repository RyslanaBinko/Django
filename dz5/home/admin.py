from django.contrib import admin
# Register your models here.
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from home.models import Student


class StudentAdmin(ModelAdmin):

    list_display = ("name", "email", "birthday", "students_social")

    def students_social(self, object):  # noqa
        if object.url:
            social = format_html("<a href='{url}'>{name}</a>",
                                 url=object.url, name=object.name)

        else:
            social = object.name
        return social


admin.site.register(Student, StudentAdmin)
