from django.urls import path
from . import views

from .views import index, create, refresh, delete, sell, create_sell

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', create, name='cadastro'),
    path('vendas/', sell, name='vendas'),
    path('modificar/<int:user_id>', refresh, name='modificar'),
    path('deletar/<int:user_id>', delete, name='deletar'),
    ]
