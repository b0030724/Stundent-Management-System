from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Module, Registration
from .forms import UserRegistrationForm, UserForm, StudentForm, LoginForm, ModuleSelectionForm, ContactForm
from rest_framework import generics
from .serializers import StudentSerializer, ModuleSerializer
from django.urls import reverse  

@login_required
def profile(request):
    # Retrieve the student's profile based on the logged-in user
    student = get_object_or_404(Student, user=request.user)
    return render(request, 'students/profile.html', {'student': student})

def logout_user(request):
    logout(request)
    return redirect('students:login')  # Redirect to login page after logout

def home(request):
    if request.user.is_authenticated:
        # User is authenticated, check if they have a student profile
        student = getattr(request.user, 'student', None)  # Get the student's profile if it exists
        if student:
            # Get modules registered by the student
            modules = Module.objects.filter(registration__student=student)
            return render(request, 'students/home.html', {'modules': modules, 'student': student})
        else:
            # User is logged in but doesn't have a student profile
            return render(request, 'students/home.html', {'message': 'You are logged in, but you don\'t have a student profile.'})
    else:
        # User is not authenticated, show a generic home page
        return render(request, 'students/home.html')

@login_required
def all_modules(request):
    modules = Module.objects.all()  # Retrieve all modules from the database
    return render(request, 'students/all_modules.html', {'modules': modules})

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
                return redirect('students:profile')  # Redirect to profile page after login
    else:
        form = LoginForm()
    return render(request, 'students/login.html', {'form': form})

def module_register(request):
    if request.method == 'POST':
        form = ModuleSelectionForm(request.POST)
        if form.is_valid():
            modules = form.cleaned_data['modules']
            student = get_object_or_404(Student, user=request.user)
            for module in modules:
                print(f"Registering {student} to {module}")  # Debugging statement
                Registration.objects.create(student=student, module=module)
            return redirect('students:home')
        else:
            print("Form errors:", form.errors)  # Debugging statement
    else:
        form = ModuleSelectionForm()
    modules = Module.objects.all()
    return render(request, 'students/module_register.html', {'form': form, 'modules': modules})

def all_modules(request):
    modules = Module.objects.all()
    return render(request, 'students/module_list.html', {'modules': modules})

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')

def some_view(request):
    return redirect('students:all_modules')

@login_required
def edit_profile(request):
    user = request.user
    student = user.student  # Assuming a one-to-one relationship between User and Student

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        student_form = StudentForm(request.POST, instance=student)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return redirect('students:profile')  # Redirect to profile page after editing
    else:
        user_form = UserForm(instance=user)
        student_form = StudentForm(instance=student)

    return render(request, 'students/edit_profile.html', {
        'user_form': user_form,
        'student_form': student_form
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=['your_email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('students:contact')
    else:
        form = ContactForm()

    return render(request, 'students/contact.html', {'form': form})

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
