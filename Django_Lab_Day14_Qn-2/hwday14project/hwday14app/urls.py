from django.contrib import admin
from django.urls import path, include 
from hwday14app import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_product/', views.create_product,name='create')
]