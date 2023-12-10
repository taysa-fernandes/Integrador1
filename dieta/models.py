from django.db import models

from alimento.models import Alimento

class Dieta(models.Model):
    STATUS_DIETA = (
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('finalizada', 'Finalizada')
    )
    
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_DIETA, default='pendente')

class Refeicao(models.Model):
    nome = models.CharField(max_length=255)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, related_name='refeicoes')
    
class AlimentoRefeicao(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)