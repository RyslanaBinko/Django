import csv

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from home.forms import StudentForm
from home.models import Student


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

    def get_student(self, id):  # noqa

        return get_object_or_404(Student, id=id)

    def get(self, request, id):  # noqa

        student = self.get_student(id)
        student_form = StudentForm(instance=student)

        context = {
            "form": student_form,
            "id": student.id,
                   }
        return render(
            request, "update_student.html", context=context,
        )

    def post(self, request, id):  # noqa
        student = self.get_student(id)  # noqa
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse("students_class"))


class JsonView(View):

    def get(self, request):
        students = Student.objects.all()

        return JsonResponse({
            "students": list(students.values(
                "name",
                "age",
                "sex",
                "email",
            )),
        })


class CSVView(View):

    def get(self, request):
        response = HttpResponse(content_type="text/csv")

        response['Content-Disposition'] = "attachment; filename=students.csv"

        writer = csv.writer(response)
        writer.writerow(["Name", "Age", "Sex", "Email"])

        students = Student.objects.all()
        for student in students:
            writer.writerow([
                student.name,
                student.age,
                student.sex,
                student.email,
            ])

        return response
