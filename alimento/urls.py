from django.contrib import admin
from django.urls import path
from  alimento.views import AlimentoCriar
urlpatterns = [
    path('cadastrar-alimento',AlimentoCriar.as_view(), name='cadastrar-alimento'),

]
