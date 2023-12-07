from django.contrib import admin
from django.urls import path
from  alimento.views import alimentos,cadastrar_alimento

urlpatterns = [
    path('cadastrar-alimento',cadastrar_alimento, name='cadastrar-alimento'),
    path('alimentos/', alimentos, name='listar-alimentos'),
]
