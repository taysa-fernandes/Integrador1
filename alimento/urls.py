from django.contrib import admin
from django.urls import path
from  alimento.views import AlimentoCriar, AlimentoListar  
urlpatterns = [
    path('cadastrar-alimento',AlimentoCriar.as_view(), name='cadastrar-alimento'),
    path('alimentos/', AlimentoListar.as_view(), name='listar-alimentos'),
]
