from django.contrib import admin
from django.urls import path
from formulario.views import meus_formularios, novo_formulario, tipo_questao

urlpatterns = [
    path('meus-formularios/',meus_formularios, name='listar-formularios'),
    path('novo-formulario/', novo_formulario, name='novo-formulario'),
    path('tipo-questao', tipo_questao, name='tipo-questao'),
]
