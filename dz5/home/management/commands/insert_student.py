from django.core.management import BaseCommand
from faker import Faker
import random

from home.models import Student


class Command(BaseCommand):

    help = "Insert student"

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        sex = ("F", "M")
        faker = Faker()
        for _ in range(options['len']):
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = random.randint(10, 99)
            student.sex = random.choice(sex)
            student.address = faker.address()
            student.birthday = faker.date()
            student.descriptions = faker.text()
            student.email = faker.email()
            student.save()
