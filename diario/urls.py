from django.contrib import admin
from django.urls import path
from  diario.views import CriarDiario, RegistrarProgressoNoDiario, AtualizarDiario, ListarDiarios

urlpatterns = [
    path('diario/', CriarDiario.as_view(), name="diario"),  
    path('criar-diario/<int:id>/', RegistrarProgressoNoDiario.as_view(), name="conteudo-diario"),  
    path('atualizar-diario/<int:id>/', AtualizarDiario.as_view(), name="atualizar-diario"),  
    path('listar-diarios/', ListarDiarios.as_view(), name="listar-diarios"),  
]
