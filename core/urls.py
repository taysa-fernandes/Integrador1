from django.contrib import admin
from django.urls import path
from  core.views import index, meus_formularios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('meus-formularios/',meus_formularios),
]