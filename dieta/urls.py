from django.contrib import admin
from django.urls import path
from  dieta.views import dieta, CadastrarDieta, ListarDietas, DefinirNumeroRefeicoes

urlpatterns = [
    path('cadastrar-dieta/', CadastrarDieta.as_view(), name='cadastrar-dieta'),
    path('ver-dieta/',dieta, name='ver-dieta'),
    path('dieta/',ListarDietas.as_view(), name='listar-dietas'),
    path('definir-numero-refeicoes/', DefinirNumeroRefeicoes.as_view(), name='definir-numero-refeicoes'),
]
