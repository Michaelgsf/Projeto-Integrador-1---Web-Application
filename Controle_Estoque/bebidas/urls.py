from django.urls import path
from . import views

from .views import index, create, refresh, delete#, relatorio_vendas

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', create, name='cadastro'),
    path('modificar/<int:user_id>', refresh, name='modificar'),
    path('deletar/<int:user_id>', delete, name='deletar'),
    ]
