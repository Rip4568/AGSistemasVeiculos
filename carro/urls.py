from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('register_new_car/', views.register_new_car, name='register_new_car'),
    path('delete_car/<int:pk>/', views.delete_car, name='delete_car'),
]
