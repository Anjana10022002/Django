from django.urls import path
from hwday10app.forms import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_students, name='edit_students'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]