from django.contrib import admin
from django.urls import path
from paciente.views import cadastrar_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar-paciente',cadastrar_paciente)
]