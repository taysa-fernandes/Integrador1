from django.contrib import admin
from django.urls import path
from  core.views import home, index, meus_formularios, novo_formulario, dieta, alimentos,cadastrar_dieta,cadastrar_alimento,cadastrar_paciente,tipo_questao, progresso, diario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
    path('',index),
    path('dieta/',dieta),
    path('cadastrar-alimento',cadastrar_alimento),
    path('meus-formularios/',meus_formularios),
    path('novo-formulario/', novo_formulario),
    path('progresso/', progresso, name="progresso"),  
    path('alimentos/', alimentos),
    path('diario/', diario, name="diario"),  
    path('tipo-questao', tipo_questao),
    path('cadastrar-dieta',cadastrar_dieta),
    path('cadastrar-paciente',cadastrar_paciente)
]