import random
import uuid

from django.core.management import BaseCommand
from faker import Faker
from home.models import Book, Student, Subject, Teacher


class Command(BaseCommand):

    help = "Insert student"  # noqa

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        sex = ("F", "M")
        faker = Faker()
        for _ in range(options['len']):
            subject, _ = Subject.objects.get_or_create(title='Python')

            book = Book()
            book.title = uuid.uuid4()
            book.save()

            teacher = Teacher()
            teacher.name = faker.name()
            teacher.save()

            student = Student()
            student.name = faker.name()
            student.age = random.randint(10, 99)
            student.sex = random.choice(sex)
            student.address = faker.address()
            student.birthday = faker.date()
            student.descriptions = faker.text()
            student.email = faker.email()
            student.url = faker.url()
            student.subject = subject
            student.book = book
            student.save()
            student.teacher.add(teacher)
