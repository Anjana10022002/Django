from django.urls import path
from cwday2app import views
urlpatterns = [
  path('', views.home),
  path('', views.aboutus),
]