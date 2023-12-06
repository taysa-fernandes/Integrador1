from django.db import models
from core.models import Usuario

class Paciente(Usuario):
    status_paciente =(
        (1, "Aguardando formulário pós consulta"),
        (2,"Aguardando formulário pré consulta"),
        (3,"Dieta em andamento"),
        (4,"Dieta concluída"),
    )
    idade = models.IntegerField()
    peso =  models.DecimalField(decimal_places=2, max_digits=6)
    altura = models.DecimalField(decimal_places=2, max_digits=6)
    cpf = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100,blank=True)
    objetivo = models.CharField(max_length=20,blank=True)
    diagnostico = models.BooleanField(default=False)
    status = models.IntegerField(choices=status_paciente,default=1,blank=True)
    