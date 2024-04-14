from django.urls import path
from . import views

app_name = 'controle'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_regisro_controle, name='delete'),
    path('update/<int:pk>/', views.update_regisro_controle, name='update'),
    path('render_form_update/<int:pk>/', views.render_form_update_controle_registro, name='render_form_update'),
    path('render_table_list/', views.render_table_list_controle_registro, name='render_table_list'),
]
