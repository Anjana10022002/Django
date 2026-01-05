from django.urls import path
from hwday4app import views

urlpatterns = [
    path('', views.input_form, name='input_form'),
    path('result/', views.result, name='result'),
]
