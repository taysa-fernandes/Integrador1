from django.contrib import admin
from django.urls import path
from  core.views import home, index, meus_formularios, novo_formulario, dieta, alimentos,cadastrar_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('',index),
    path('meus-formularios/',meus_formularios),
    path('novo-formulario/', novo_formulario),
    path('dieta',dieta),
    path('progresso',progresso, name="progresso"),
    path('diario',diario,name="diario"),
    path('alimentos/', alimentos)
    path('cadastrar-paciente',cadastrar_paciente)
]
