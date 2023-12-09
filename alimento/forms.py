from django.forms import ModelForm
from .models import Alimento

class AlimentoForm(ModelForm):

    class Meta:
        model = Alimento
        fields = '__all__'