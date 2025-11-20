from django.urls import path
from teachers import views

app_name = 'teachers'

urlpattern = [
    path('', views.teachers_list, name = "teachers_list")
]