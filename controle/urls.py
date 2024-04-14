from django.urls import path
from . import views

app_name = 'controle'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_regisro_controle, name='delete'),
    path('update/<int:pk>/', views.update_regisro_controle, name='update'),
]
