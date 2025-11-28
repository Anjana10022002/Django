from django.contrib import admin
from django.urls import path, include 
from hwday14app import views  

urlpatterns = [
    path('', views.create_product, name='home'),
    path('create_product/', views.create_product, name='create'),
    path('admin/', admin.site.urls),
    path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('product/<int:pk>/', views.product_detail, name='product_details'),
    path('product/<int:pk>/email/', views.send_product_email, name='send_email'),
]

# urlpatterns += [
#     path('fileupload/', include('profilemaker.urls')),
# ]