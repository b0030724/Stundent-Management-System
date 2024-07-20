# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Module, Registration
from .forms import UserRegistrationForm, StudentForm, LoginForm, ModuleRegistrationForm
from rest_framework import generics
from .serializers import StudentSerializer, ModuleSerializer

def all_modules(request):
    modules = Module.objects.all()  # Retrieve all modules from the database
    return render(request, 'students/all_modules.html', {'modules': modules})

@login_required
def home(request):
    student = Student.objects.get(user=request.user)
    # Get modules registered by the student
    modules = Module.objects.filter(registration__student=student)
    return render(request, 'students/home.html', {'modules': modules})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user  # Link student to the newly created user
            student.save()
            login(request, user)  # Log the user in after registration
            return redirect('students:home')  # Redirect to the home page
    else:
        user_form = UserRegistrationForm()
        student_form = StudentForm()
    return render(request, 'students/register.html', {'user_form': user_form, 'student_form': student_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('students:home')
    else:
        form = LoginForm()
    return render(request, 'students/login.html', {'form': form})

@login_required
def module_register(request):
    if request.method == 'POST':
        # Collect selected modules from the POST data
        module_ids = request.POST.getlist('modules')
        for module_id in module_ids:
            module = Module.objects.get(id=module_id)
            Registration.objects.create(student=request.user.student, module=module)
        return redirect('students:home')
    else:
        modules = Module.objects.all()
        return render(request, 'students/module_register.html', {'modules': modules})

@login_required
def logout_user(request):
    logout(request)
    return redirect('students:login')

# DRF Views
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ModuleList(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
