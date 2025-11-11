from django.urls import path
from cwday2app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
