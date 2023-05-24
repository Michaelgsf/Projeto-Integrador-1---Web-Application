from django.urls import path
from . import views

from .views import index, cadastro, refresh, delete, sell

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('vendas/', sell, name='vendas'),
    path('modificar/<int:user_id>', refresh, name='modificar'),
    path('deletar/<int:user_id>', delete, name='deletar'),
    ]
