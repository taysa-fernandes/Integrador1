from django.contrib import admin
from django.urls import path
from  core.views import index,dieta
from  core.views import index,diario

urlpatterns = [
    path('',index),
    path('dieta',dieta),
    path('diario',diario)
]