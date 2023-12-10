from django import forms
from .models import Nutricionista

class NutricionistaForm(forms.ModelForm):
    class Meta:
        model = Nutricionista
        fields = ['nome', 'email', 'contato', 'senha', 'crn']  
