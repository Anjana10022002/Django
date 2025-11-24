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
    # path('about-us/', views.aboutUs,name='about-us'),
    path('', views.pagevisit, name='home'),
    path('pagevisit/',views.pagevisit,name='page_visit')
]