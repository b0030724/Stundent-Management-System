from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse
from django.http import HttpResponse

from .models import Student, Module, Registration, Course
from .forms import UserRegistrationForm, UserForm, StudentForm, LoginForm, ModuleSelectionForm, ContactForm
from rest_framework import generics
from .serializers import StudentSerializer, ModuleSerializer

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    # Get all modules associated with this course
    modules = course.modules.all()
    # Get all registrations for these modules
    registrations = Registration.objects.filter(module__in=modules)
    # Get all students for these registrations
    registered_students = Student.objects.filter(registration__in=registrations)

    return render(request, 'students/course_detail.html', {
        'course': course,
        'registered_students': registered_students,
    })
@login_required
def profile(request):
    student = get_object_or_404(Student, user=request.user)
    return render(request, 'students/profile.html', {'student': student})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('students:home')

from django.core.paginator import Paginator

def home(request):
    if request.user.is_authenticated:
        try:
            student = request.user.student
            modules = Module.objects.filter(registration__student=student)
            courses = Course.objects.all()

            # Pagination
            paginator = Paginator(courses, 5)  # Show 5 courses per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'students/home.html', {
                'modules': modules,
                'courses': page_obj,
                'student': student,
                'page_obj': page_obj,  # Pass page_obj to the template
            })
        except Student.DoesNotExist:
            paginator = Paginator(Course.objects.all(), 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'students/home.html', {
                'courses': page_obj,
                'message': "You are logged in, but you don't have a student profile.",
                'page_obj': page_obj,
            })
    else:
        paginator = Paginator(Course.objects.all(), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'students/home.html', {
            'courses': page_obj,
            'page_obj': page_obj,
        })

@login_required
def all_modules(request):
    modules = Module.objects.all()
    return render(request, 'students/all_modules.html', {'modules': modules})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('students:home')
        else:
            print(user_form.errors)
            print(student_form.errors)
            messages.error(request, 'Please correct the errors below.')
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
                messages.success(request, f"Welcome back, {user.username}!")
                print("User logged in, success message added.")
                return redirect('students:home')
            else:
                messages.error(request, "Invalid username or password.")
                print("Invalid login attempt.")
    else:
        form = LoginForm()
    return render(request, 'students/login.html', {'form': form})


@login_required
def module_register(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, 'You must have a student profile to register for modules.')
        return redirect('students:home')

    if request.method == 'POST':
        form = ModuleSelectionForm(request.POST)
        if form.is_valid():
            modules = form.cleaned_data['modules']
            for module in modules:
                Registration.objects.create(student=student, module=module)
            return redirect('students:home')
    else:
        form = ModuleSelectionForm()

    modules = Module.objects.all()
    return render(request, 'students/module_register.html', {'form': form, 'modules': modules})

def about(request):
    return render(request, 'students/about.html')

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
                recipient_list=['b0030724@my.shu.uk'],  
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('students:success')
    else:
        form = ContactForm()

    return render(request, 'students/contact.html', {'form': form})

def success(request):
    return HttpResponse('Success! Your message has been sent.')

@login_required
def edit_profile(request):
    user = request.user
    try:
        student = user.student
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('students:home')

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        student_form = StudentForm(request.POST, instance=student)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return redirect('students:profile')
    else:
        user_form = UserForm(instance=user)
        student_form = StudentForm(instance=student)

    return render(request, 'students/edit_profile.html', {
        'user_form': user_form,
        'student_form': student_form
    })

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
