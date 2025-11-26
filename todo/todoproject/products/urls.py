from django.urls import path
from . import views
urlpatterns = [
    path('create_products', views.create_product, name='createproductapi'),
]