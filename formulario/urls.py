from django.contrib import admin
from django.urls import path
from formulario.views import tipo_questao, FormularioCriar, FormularioListar

urlpatterns = [
    # path('meus-formularios/',meus_formularios, name='meus-formularios'),
    # path('novo-formulario/', novo_formulario, name='novo-formulario'),
    path('formularios/cadastrar/', FormularioCriar.as_view(), name='cadastrar-formulario'),
    path('formularios/', FormularioListar.as_view(), name='listar-formularios'),
    path('tipo-questao', tipo_questao, name='tipo-questao'),
]
