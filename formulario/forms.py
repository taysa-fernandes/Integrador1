from django import forms
from .models import Pergunta,Resposta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = '__all__'
        
class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'