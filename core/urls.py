from django.contrib import admin
from django.urls import path
from  core.views import home, index, meus_formularios, novo_formulario, dieta, alimentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('',index),
    path('meus-formularios/',meus_formularios),
    path('novo-formulario/', novo_formulario),
    path('dieta',dieta),
    path('alimentos/', alimentos)
]