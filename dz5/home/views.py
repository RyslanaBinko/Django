from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from home.models import Student


def home(request):
    student = Student()
    student.name = "Lana"
    student.save()
    students = Student.objects.all()
    return render(request, "index.html", context={"students": students, })
