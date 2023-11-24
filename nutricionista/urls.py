from django.contrib import admin
from django.urls import path
from  core.views import cadastrar_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar-paciente',cadastrar_paciente)
]