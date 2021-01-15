from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse
from django.views import View

from home.models import Student
from home.forms import StudentForm


class HomeView(View):

    """
    class to display the list of students,
    with the ability to go to the student update page;
    """

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

    """
    class for updating a student according to his id;
    get request to display student change form;
    post request to go to the list of students;

    returns a list of students with saved changes;
    """

    def get_student(self, id):

        return get_object_or_404(Student, id=id)

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
