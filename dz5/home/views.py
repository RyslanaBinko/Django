import csv
from time import sleep

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from home.forms import StudentForm
from home.models import Student
from home.send_email import email


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


class SendEmailView(View):
    def get(self, request):
        email(recipient_list=['binko.ryslana@gmail.com', ])
        return HttpResponse('Email send')


class StudentView(ListView):
    sleep(10)

    model = Student
    template_name = 'index.html'


class StudentCreateView(CreateView):

    model = Student
    fields = ['name', 'birthday', 'email']
    template_name = 'student_create.html'
    success_url = reverse_lazy('student_view')


class StudentUpdateView(UpdateView):

    model = Student
    fields = ['name', 'birthday', 'email']
    template_name = 'update_student.html'
    success_url = reverse_lazy('student_view')


class StudentDeleteView(DeleteView):

    model = Student
    success_url = reverse_lazy('student_view')
    template_name = 'student_delete.html'
