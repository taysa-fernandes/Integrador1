from django.contrib import admin
from django.urls import path
from core.views import index
from paciente.views import PacienteListar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', PacienteListar.as_view(), name='listar-pacientes'),
]
