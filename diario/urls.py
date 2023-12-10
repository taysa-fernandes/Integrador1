from django.contrib import admin
from django.urls import path
from  diario.views import Diario

urlpatterns = [
    path('diario/', Diario.as_view(), name="diario"),  
]
