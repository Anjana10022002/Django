from django.urls import path
from certificates import views
urlpatterns = [
    # path('',views.certificate_create,name='create'),
    path('', views.certificate_create, name='certificate_create'),
    path('download_pdf', views.download_pdf, name='download_pdf'),
    path('certificate/<int:pk>/pdf/', views.download_pdf, name='download_pdf'),
    path('certificate/<int:pk>/', views.cert_details_view, name='cert_details'),
    path('certificate/<int:pk>/send_email/', views.send_certificate_email, name='send_certificate_email')
]