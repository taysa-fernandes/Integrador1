from django.forms import ModelForm
from .models import Opcao

class OpcaoForm(ModelForm):

    class Meta:
        model = Opcao
        fields = '__all__'