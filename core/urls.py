from django.contrib import admin
from django.urls import path
from  core.views import home, index, progresso, diario, meus_formularios, novo_formulario, dieta, alimentos,cadastrar_paciente, cadastrar_alimento, tipo_questao, cadastrar_dieta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
    path('',index),
    path('dieta/',dieta),
    path('cadastrar-alimento',cadastrar_alimento),
    path('meus-formularios/',meus_formularios),
    path('novo-formulario/', novo_formulario),
    path('dieta',dieta),
    path('progresso',progresso),
    path('diario/',diario),
    path('alimentos/', alimentos),
    path('diario/', diario, name="diario"),  
    path('tipo-questao', tipo_questao),
    path('cadastrar-dieta',cadastrar_dieta),
    path('cadastrar-paciente',cadastrar_paciente)
]
