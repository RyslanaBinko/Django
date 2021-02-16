from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)  # noqa
    name = models.CharField(max_length=200)
    normalized_name = models.CharField(max_length=200, null=True)
    age = models.SmallIntegerField(null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    email = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
