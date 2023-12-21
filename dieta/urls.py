from django.contrib import admin
from django.urls import path
from  dieta.views import dieta, CadastrarDieta, ListarDietas, EditarDieta, DeletarDieta, DefinirNumeroRefeicoes

urlpatterns = [
    path('cadastrar-dieta', CadastrarDieta.as_view(), name='cadastrar-dieta'),
    path('editar-dieta/<int:dieta_id>/', EditarDieta.as_view(), name='editar-dieta'),
    path('dieta/',ListarDietas.as_view(), name='listar-dietas'),
    path('deletar-dieta/<int:id>/', DeletarDieta.as_view(), name='deletar-dieta'),
    path('ver-dieta/',dieta, name='ver-dieta'),
    path('definir-numero-refeicoes', DefinirNumeroRefeicoes.as_view(), name='definir-numero-refeicoes'),
]
