from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('register_new_car/', views.register_new_car, name='register_new_car'),
    path('delete_car/<int:pk>/', views.delete_car, name='delete_car'),
    path('update_car/<int:pk>/', views.update_car, name='update_car'),
    path('render_form_update_car/<int:pk>/', views.render_form_update_car, name='render_form_update_car'),
]
