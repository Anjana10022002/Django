from django.contrib import admin
from django.urls import path
from cwday8app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutus', views.aboutus, name = 'aboutus'), 

]
