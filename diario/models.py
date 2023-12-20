from django.db import models
from alimento.models import Alimento
from paciente.models import Paciente
from dieta.models import Refeicao

# Create your models here.
class Diario(models.Model):
    data = models.DateTimeField(editable=False)
    calorias_consumidas = models.IntegerField(default=0)
    alimentos = models.ManyToManyField(Alimento)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=16)
    refeicoes = models.ManyToManyField(Refeicao, related_name='diarios', blank=True)