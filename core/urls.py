from django.contrib import admin
from django.urls import path
from core.views import index
from paciente.views import PacienteListar
from alimento.views import AlimentoListar
from .views import NutricionistaCriar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('home/', PacienteListar.as_view(), name='listar-pacientes'),
    path('alimentos/', AlimentoListar.as_view(), name='listar-alimentos'),
    path('cadastrar-se',NutricionistaCriar.as_view(), name='cadastrar-se'),
]
