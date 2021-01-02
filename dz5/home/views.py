from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse
from django.views import View

from home.models import Student
from home.forms import StudentForm


class HomeView(View):
    def get(self, request):
        students = Student.objects.all()
        student_form = StudentForm()

        context = {
            "students": students,
            "form": student_form,
                   }
        return render(request, "index.html", context=context)

    def post(self, request):
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse("students_class"))


class UpdateView(View):

    def get_student(self, id):

        return Student.objects.get(id=id)

    def get(self, request, id):
        student = self.get_student(id)
        student_form = StudentForm(instance=student)

        context = {
            "form": student_form,
            "id": student.id,
                   }
        return render(
            request, "update_student.html", context=context,
        )

    def post(self, request, id):
        student = self.get_student(id)
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse("students_class"))
