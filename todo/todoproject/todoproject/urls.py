# from django.urls import path
# from greeting import views
# urlpatterns = [
#   path('', views.greeting),
# ]

from django.contrib import admin
from django.urls import path
from greeting import views
urlpatterns = [
    # path('', views.greeting,name='home'),
    path('aboutus/', views.aboutUs,name='about-us'),
    path('pagevist/', views.pagevisit, name='home'),
    path('signup/',views.signup_page,name='signup' ),
    path('login/',views.login_page,name='login' ),  
]