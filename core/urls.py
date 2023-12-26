from django.contrib import admin
from django.urls import path
from .views import Index, AutenticarUsuario, Logout
from paciente.views import PacienteListar
from alimento.views import AlimentoListar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('home/', PacienteListar.as_view(), name='listar-pacientes'),
    path('alimentos/', AlimentoListar.as_view(), name='listar-alimentos'),
    path('login/', AutenticarUsuario.as_view(), name='autenticar-usuario'),
    path('logout/', Logout.as_view(), name='logout'),
]
