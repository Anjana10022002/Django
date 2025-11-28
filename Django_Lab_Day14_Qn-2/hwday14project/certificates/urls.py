from django.urls import path
from certificates import views
urlpatterns = [
    path('',views.certificate_create,name='create'),
    path('download_pdf', views.download_pdf, name='download_pdf'),
    path('send_mail', views.send_mail, name ='send_mail'),
]