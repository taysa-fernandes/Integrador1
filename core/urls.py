from django.contrib import admin
from django.urls import path
from  core.views import index
from core.views import index
from paciente.views import PacienteListar
from alimento.views import AlimentoListar
from .views import autenticar_usuario, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', PacienteListar.as_view(), name='listar-pacientes'),
    path('alimentos/', AlimentoListar.as_view(), name='listar-alimentos'),
    path('login/', autenticar_usuario, name='autenticar-usuario'),
    path('logout/', logout_view, name='logout'),
]
