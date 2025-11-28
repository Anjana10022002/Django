from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_create, name='root'),
    path('home/', views.product_create, name='home'),
    path('products/create_products/', views.product_create, name='createproductapi'),
    path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    ]