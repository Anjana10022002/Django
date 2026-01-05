from django.contrib import admin
from django.urls import path
from hwday7app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cus_details, name='add_customers'),
    # path('add/', views.cus_deatils, name = 'add_customers'),
    path('all/', views.all_customers, name = 'all_customers'), 
    path('filtered/', views.filt_customers, name = 'filtered_customers')
]