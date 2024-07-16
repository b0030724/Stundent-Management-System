# students/urls.py

from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    # Other URL patterns as needed
]
