from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('all_modules/', views.all_modules, name='all_modules'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('module_register/', views.module_register, name='module_register'),
    path('logout/', views.logout_user, name='logout'),
    
    # API URLs
    path('api/students/', views.StudentList.as_view(), name='api_student_list'),
    path('api/students/<int:pk>/', views.StudentDetail.as_view(), name='api_student_detail'),
    path('api/modules/', views.ModuleList.as_view(), name='api_module_list'),
    path('api/modules/<int:pk>/', views.ModuleDetail.as_view(), name='api_module_detail'),
]

