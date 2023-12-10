
from django.urls import path
from  alimento.views import AlimentoCriar,AlimentoDeletar,AlimentoEditar
urlpatterns = [
    path('alimentos/cadastrar',AlimentoCriar.as_view(), name='cadastrar-alimento'),
    path('alimentos/deletar/<int:id>',AlimentoDeletar.as_view(), name='deletar-alimento'),
    path('alimentos/editar/<int:id>',AlimentoEditar.as_view(), name='editar-alimento'),
]
