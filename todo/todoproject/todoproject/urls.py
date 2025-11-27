# from django.urls import path
# from greeting import views
# urlpatterns = [
#   path('', views.greeting),
# ]

from django.contrib import admin
from django.urls import path, include
from greeting import views
from products import views
# urlpatterns = [
#     # path('', views.greeting,name='home'),
#     path('aboutus/', views.aboutUs,name='about-us'),
#     path('pagevist/', views.pagevisit, name='home'),
#     path('signup/',views.signup_page,name='signup' ),
#     path('login/',views.login_page,name='login' ),
# ]
urlpatterns = [
    path('create_products/', views.product_create, name='createproductapi'),
    path('productsapi/', include('productsapi.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]  
