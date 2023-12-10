from django import forms
from .models import Pergunta,Resposta

class PerguntaForm(forms.ModelForm):
    
    class Meta:
        model = Pergunta
        fields = '__all__'
        widgets = {
            'tipo': forms.RadioSelect(choices=Pergunta.TIPOS_FORMULARIO),
        }
    def save(self, commit=True):
        pergunta_principal = super().save(commit=False)
        if 'tipo-pergunta' in self.data and self.data['tipo-pergunta'] == 'on':
            pergunta_principal.obrigatorio = True
        
        if commit:
            pergunta_principal.save()

        for field_name, field_value in self.data.items():
            if field_name.startswith('pergunta_'):
                nova_pergunta = Pergunta(pergunta=field_value, pergunta_principal=pergunta_principal)
                nova_pergunta.save()

        return pergunta_principal


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['resposta']