from django.contrib import admin
from django.urls import path, include 
from hwday14app import views  

urlpatterns = [
    path('', views.create_product, name='home'),
    path('create_product/', views.create_product, name='create'),
    path('admin/', admin.site.urls),
]