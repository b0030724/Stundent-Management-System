from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Module, Registration



# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Form for Editing User Details (username and email)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# Form for Student Profile
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'phone', 'address', 'date_of_birth', 'course']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        if commit:
            student.save()
        return student

# Module Registration Form (used for registering students for modules)
class ModuleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['module', 'date_of_registration']
        widgets = {
            'date_of_registration': forms.DateInput(attrs={'type': 'date'}),
        }

# Module Form (used for creating or editing modules)
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['code', 'name', 'description', 'credits', 'semester', 'instructor']

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

# Module Selection Form (selecting up to two modules)
class ModuleSelectionForm(forms.Form):
    modules = forms.ModelMultipleChoiceField(
        queryset=Module.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select up to two modules",
        help_text="You can only select two modules.",
    )

    def clean_modules(self):
        data = self.cleaned_data['modules']
        if len(data) != 2:
            raise forms.ValidationError("You must select exactly two modules.")
        return data

# Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15, required=False, label="Your Phone Number")
    subject = forms.CharField(max_length=100, required=True, label="Subject")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your Message")
