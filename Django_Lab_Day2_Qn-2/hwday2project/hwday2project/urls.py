from django.urls import path
from hwday2project import views

urlpatterns = [
    path('gallerypage/', views.gallerypage, name='gallery'),
    path('contactme/', views.contactme, name='contact'),
]
