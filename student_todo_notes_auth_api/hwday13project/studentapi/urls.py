from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('add_note',views.add_note,name='add_note'),
    path('note_list',views.note_list,name='note_list'),
    path('create_product', views.create_product,name='create_product')
]

