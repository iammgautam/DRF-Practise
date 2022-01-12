from django.urls import path
from .views import student_detail, student_list

urlpatterns = [
    path('',student_list, name='list'),
    path('<int:id>/', student_detail, name='detail'),
]