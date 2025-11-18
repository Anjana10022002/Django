from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('view_books/', views.view_books, name='view_books'),
]