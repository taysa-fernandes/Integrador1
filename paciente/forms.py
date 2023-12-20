from django.forms import ModelForm
from .models import Paciente

class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ['data_criacao']