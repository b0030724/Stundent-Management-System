from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Student
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html',{
     'students': Student.objects.all()})
    
def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/student_detail.html', {'student': student})
