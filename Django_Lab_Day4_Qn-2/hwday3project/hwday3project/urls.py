from django.urls import path
from hwday3project import views

urlpatterns = [
    path('', views.input_form, name='input_form'),
    path('result/', views.result, name='result'),
]
