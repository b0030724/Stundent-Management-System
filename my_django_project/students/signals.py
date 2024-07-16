from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Module, Student

@receiver(m2m_changed, sender=Module.students.through)
def limit_student_modules(sender, instance, action, reverse, pk_set, **kwargs):
    if action == 'pre_add':
        if not reverse:  # Adding modules to a student
            if instance.students.count() >= 2:
                raise ValidationError("A student cannot be enrolled in more than 2 modules.")
        else:  # Adding students to a module
            for student_id in pk_set:
                student = Student.objects.get(pk=student_id)
                if student.modules.count() >= 2:
                    raise ValidationError(f"Student {student} cannot be enrolled in more than 2 modules.")
