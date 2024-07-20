from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Module, Registration
from datetime import date

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'age', 'email', 'phone', 'address', 'date_of_birth', 'course']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ModuleRegistrationForm(forms.ModelForm):
    date_of_registration = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )

    class Meta:
        model = Module
        fields = ['code', 'name', 'description', 'credits', 'semester', 'instructor']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

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


    class Meta:
        model = Module
        fields = ['code', 'name', 'description', 'credits', 'semester', 'instructor']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
