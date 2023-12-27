from django.db import models

from alimento.models import Alimento
from paciente.models import Paciente

class Dieta(models.Model):
    STATUS_DIETA = (
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('finalizada', 'Finalizada')
    )
    
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_DIETA, default='andamento')
    paciente = models.ManyToManyField(Paciente, related_name='dietas')

class Refeicao(models.Model):
    nome = models.CharField(max_length=255)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, related_name='refeicoes', blank=True)
    alimentos = models.ManyToManyField(Alimento, related_name='refeicoes')