import re

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from home.models import Student


@receiver(pre_save, sender=Student)
def normalized_name(sender, instance, **kwargs):
    instance.normalized_name = re.sub('[^\w\s]|_', '', instance.name).lower()


@receiver(pre_delete, sender=Student)
def delete_student(sender, instance, **kwargs):
    raise Exception("You can't delete a student")
    return None