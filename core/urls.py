from django.contrib import admin
from django.urls import path
from core.views import index
from paciente.views import PacienteListar
from alimento.views import AlimentoListar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', PacienteListar.as_view(), name='listar-pacientes'),
    path('alimentos/', AlimentoListar.as_view(), name='listar-alimentos'),
]
