from django import forms
from django.forms import ModelForm
from .models import Formulario

class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'