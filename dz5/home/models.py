from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)  # noqa
    name = models.CharField(max_length=200)
    normalized_name = models.CharField(max_length=200, null=True)
    age = models.SmallIntegerField(null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    email = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)

    subject = models.ForeignKey("home.Subject",
                                on_delete=models.SET_NULL, null=True)
    book = models.OneToOneField("home.Book",
                                on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField("home.Teacher")


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)  # noqa
    name = models.CharField(max_length=200, null=True)


class Subject(models.Model):
    id = models.AutoField(primary_key=True)  # noqa
    title = models.CharField(max_length=200)


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # noqa
    title = models.CharField(max_length=200, null=True)
