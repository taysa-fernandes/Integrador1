from django.contrib import admin
from django.urls import path
from  core.views import index,dieta,progresso,diario

urlpatterns = [
    path('',index),
    path('dieta',dieta),
    path('progresso',progresso, name="progresso"),
    path('diario',diario,name="diario"),
]