"""ProjectDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import (CSVView, HomeView, JsonView, SendEmailView,
                        StudentCreateView, StudentDeleteView,
                        StudentUpdateView, StudentView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/class', HomeView.as_view(), name="students_class"),
    path('student/update/<pk>', StudentUpdateView.as_view(),
         name="update_student"),
    path('json_view', JsonView.as_view(), name='json_view'),
    path('csv_view', CSVView.as_view(), name='csv_view'),
    path('send_email', SendEmailView.as_view(), name='send_email'),
    path('student_view', StudentView.as_view(), name='student_view'),
    path('student_create', StudentCreateView.as_view(),
         name='student_create'),
    path('student_delete/<pk>', StudentDeleteView.as_view(),
         name='student_delete'),
]
