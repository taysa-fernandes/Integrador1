from django.contrib import admin
from django.urls import path
from formulario.views import ListarFormularios, CriarFormulario, tipo_questao, DefinirNumeroQuestoes

urlpatterns = [
    path('meus-formularios/', ListarFormularios.as_view(), name='listar-formularios'),
    path('novo-formulario/', CriarFormulario.as_view(), name='criar-formulario'),
    path('tipo-questao', tipo_questao, name='tipo-questao'),
    path('definir-numero-questoes', DefinirNumeroQuestoes.as_view(), name='definir-numero-questoes'),
]
