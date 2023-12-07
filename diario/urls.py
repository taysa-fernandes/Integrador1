from django.contrib import admin
from django.urls import path
from  diario.views import diario

urlpatterns = [
    path('diario/', diario, name="diario"),  
]
