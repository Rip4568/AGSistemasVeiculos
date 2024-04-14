
from django.urls import path
from . import views

app_name = 'motorista'

urlpatterns = [
    path('', views.register_and_list_motorista, name='register_and_list_motorista'),
    path('delete/<int:pk>/', views.delete_motorista, name='delete'),
]
