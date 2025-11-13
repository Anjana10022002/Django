from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallerypage, name='gallery'),
    path('contact/', views.contactpage, name='contact'),
]


