from django.core.management import BaseCommand
from home.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):

        first_student = Student.objects.first()
        first_student.delete()
