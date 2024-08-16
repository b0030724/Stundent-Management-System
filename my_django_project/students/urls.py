from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
   
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('modules/', views.all_modules, name='all_modules'),
    path('module_register/', views.module_register, name='module_register'),
     path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # API URLs
    path('api/students/', views.StudentList.as_view(), name='api_student_list'),
    path('api/students/<int:pk>/', views.StudentDetail.as_view(), name='api_student_detail'),
    path('api/modules/', views.ModuleList.as_view(), name='api_module_list'),
    path('api/modules/<int:pk>/', views.ModuleDetail.as_view(), name='api_module_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
