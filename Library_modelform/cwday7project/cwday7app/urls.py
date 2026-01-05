from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='add_book'),
    path('books/', views.view_books, name='view_books'),
]