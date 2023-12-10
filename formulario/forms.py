from django import forms
from .models import Pergunta,Resposta,Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['tipo']

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['pergunta', 'obrigatorio']


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['resposta']