
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    uuser = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Provide a default user ID
    student_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Module(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    semester = models.CharField(max_length=20)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date_of_registration = models.DateField()

    def __str__(self):
        return f"{self.student.user.username} - {self.module.name}"
