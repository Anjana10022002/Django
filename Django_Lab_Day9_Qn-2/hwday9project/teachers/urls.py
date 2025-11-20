from django.urls import path
from teachers import views

urlpatterns = [
    path("", views.teachers_list, name="teachers_list"),
]