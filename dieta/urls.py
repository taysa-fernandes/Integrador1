from django.contrib import admin
from django.urls import path
from  dieta.views import dieta, cadastrar_dieta

urlpatterns = [
    path('cadastrar-dieta',cadastrar_dieta, name='cadastrar-dieta'),
    path('dieta/',dieta, name='listar-dietas'),
]
