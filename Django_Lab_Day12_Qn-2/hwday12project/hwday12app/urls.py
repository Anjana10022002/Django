from django.urls import path
from . import views

urlpatterns = [
    path('new_account/', views.new_account, name='new_account'),
    path('login/', views.login, name='login'),  
]