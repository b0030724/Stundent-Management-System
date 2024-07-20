from django.contrib import admin
from .models import Student, Module, Registration

class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 1

class ModuleAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    list_display = ('code', 'name', 'credits', 'semester', 'instructor')
    search_fields = ('code', 'name', 'instructor')

class StudentAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    list_display = ('student_number', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('student_number', 'first_name', 'last_name', 'email')

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)

