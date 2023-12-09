from django.forms import ModelForm
from .models import Dieta

class DietaForm(ModelForm):

    class Meta:
        model = Dieta
        fields = '__all__'