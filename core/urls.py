from django.contrib import admin
from django.urls import path
from  core.views import index,diario

urlpatterns = [
    path('',index),
    path('diario',diario)
]