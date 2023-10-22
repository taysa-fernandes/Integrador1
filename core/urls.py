from django.contrib import admin
from django.urls import path
from core.views import home, index, progresso, diario, meus_formularios, novo_formulario, dieta, alimentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
    path('novo-formulario/', novo_formulario),
    path('meus-formularios/', meus_formularios),
    path('alimentos/', alimentos),
    path('dieta/', dieta),  
    path('diario/', diario, name="diario"),  
    path('progresso/', progresso, name="progresso"),  
]