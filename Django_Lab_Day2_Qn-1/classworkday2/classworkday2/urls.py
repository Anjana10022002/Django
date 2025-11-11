from django.urls import path
from changeGreeting import views
urlpatterns = [
  path('', views.changeGreeting)
]