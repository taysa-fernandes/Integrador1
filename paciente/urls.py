
from django.urls import path
from paciente.views import cadastrar_paciente

urlpatterns = [
    path('cadastrar-paciente',cadastrar_paciente)
]