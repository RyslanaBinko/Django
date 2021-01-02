from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


from home.models import Student
from home.forms import StudentForm


def home(request):
    if request.method == "GET":
        student = Student()
        student.name = "Lana"
        student.save()
        students = Student.objects.all()
        student_form = StudentForm()

        context = {"students": students,
                   'form': student_form,
                   }
        return render(request, "index.html", context=context)
    elif request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        return redirect("/home")
