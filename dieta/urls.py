from django.contrib import admin
from django.urls import path
from  dieta.views import dieta, cadastrar_dieta, listar_dietas, definir_numero_refeicoes

urlpatterns = [
    path('cadastrar-dieta',cadastrar_dieta, name='cadastrar-dieta'),
    path('ver-dieta/',dieta, name='ver-dieta'),
    path('dieta/',listar_dietas, name='listar-dietas'),
    path('definir-numero-refeicoes',definir_numero_refeicoes, name='definir-numero-refeicoes'),
]
