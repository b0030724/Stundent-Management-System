from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    student_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField(default='2000-01-01')
    course = models.CharField(max_length=50)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

class Module(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    semester = models.CharField(max_length=20)
    instructor = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='modules', through='Registration')

    def __str__(self):
        return f"{self.code} - {self.name}"

class Registration(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    date_of_registration = models.DateField()

    def __str__(self):
        return f'{self.student} registered for {self.module} on {self.date_of_registration}'
