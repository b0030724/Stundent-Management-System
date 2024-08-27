from django.contrib import admin
from .models import Student, Module, Registration, Course

class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 1

class ModuleAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
    list_display = ('code', 'name', 'credits', 'semester', 'instructor')
    search_fields = ('code', 'name', 'instructor')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'get_first_name', 'get_last_name', 'get_email', 'course')
    search_fields = ('student_number', 'user__first_name', 'user__last_name', 'user__email', 'course__name')

    # Methods to display the related User model fields
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Course)  


