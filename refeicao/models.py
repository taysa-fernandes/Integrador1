from django.db import models
from alimento.models import Alimento

class Opcao(models.Model):
    nome = models.CharField(max_length=255)
    substituto = models.ForeignKey(Alimento,on_delete= models.CASCADE)
    id_opcao = models.IntegerField()
    
    def __str__(self):
        return self.nome
                                   