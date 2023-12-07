
from django.urls import path
from paciente.views import PacienteCriar,PacienteDeletar,PacienteEditar,PacienteListar

urlpatterns = [
    path('pacientes/cadastrar/',PacienteCriar.as_view(), name='cadastrar-paciente'),
    path('home/',PacienteListar.as_view(), name='listar-pacientes'),
    path('pacientes/editar/<int:id>', PacienteEditar.as_view(), name='editar-paciente'),
    path('pacientes/deletar/<int:id>',PacienteDeletar.as_view(), name='deletar-paciente'),
]