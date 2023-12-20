from typing import Any
from django.forms import ModelForm
from diario.models import Diario 
from django.db.models import Sum
from django.core.exceptions import ValidationError

class DiarioForm(ModelForm):
    class Meta:
        model = Diario
        exclude = ['calorias_consumidas', 'paciente']
                
    def save(self, commit: bool = ...) -> Any:
        
        instancia_diario = super().save(commit)
        
        calorias = instancia_diario.alimentos.aggregate(Sum('calorias'))['calorias__sum']
        
        instancia_diario.calorias_consumidas = calorias
        
        instancia_diario.save()
            
        return instancia_diario
    
    def clean_seu_campo(self):
        valor = self.cleaned_data.get('seu_campo')
        if not valor:
            raise ValidationError('Este campo é obrigatório.')
        return valor