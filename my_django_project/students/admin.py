from django.contrib import admin
from .models import Module, Student

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits', 'semester', 'instructor')
    search_fields = ('code', 'name', 'instructor')
    filter_horizontal = ('students',)  # To make the many-to-many field easier to manage

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'first_name', 'last_name', 'email', 'course')
    search_fields = ('student_number', 'first_name', 'last_name', 'email')
