from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Student, Module, Registration
from .forms import UserRegistrationForm, StudentForm, LoginForm, ModuleRegistrationForm
from rest_framework import generics
from .serializers import StudentSerializer, ModuleSerializer

def all_modules(request):
    modules = Module.objects.all()  # Retrieve all modules from the database
    return render(request, 'students/all_modules.html', {'modules': modules})

# Home View
@login_required
def home(request):
    return render(request, 'students/home.html')

# User Registration View
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

# User Login View
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
        form = ModuleRegistrationForm(request.POST)
        if form.is_valid():
            module = form.save()
            # Create a Registration instance linking the logged-in student to the module
            Registration.objects.create(student=request.user.student, module=module, date_of_registration=request.POST.get('date_of_registration'))
            return redirect('students:home')  # Redirect to home after module registration
    else:
        form = ModuleRegistrationForm()
    return render(request, 'students/module_register.html', {'form': form})

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
