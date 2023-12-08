
from django.urls import path
from  alimento.views import AlimentoCriar,AlimentoDeletar
urlpatterns = [
    path('cadastrar-alimento',AlimentoCriar.as_view(), name='cadastrar-alimento'),
    path('alimentos/deletar/<int:id>',AlimentoDeletar.as_view(), name='deletar-alimento')
]
