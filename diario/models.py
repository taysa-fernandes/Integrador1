from django.db import models
from alimento.models import Alimento
from paciente.models import Paciente

# Create your models here.
class Diario(models.Model):
    data = models.DateTimeField(editable=False)
    calorias_consumidas = models.IntegerField(default=0)
    alimentos = models.ManyToManyField(Alimento)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=16)
    refeicoes_do_dia = models.JSONField(default=list)