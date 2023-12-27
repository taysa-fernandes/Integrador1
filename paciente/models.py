from collections.abc import Iterable
from django.db import models
from django.conf import settings
class Paciente(models.Model):
    status_paciente =(
        (1, "Aguardando formulário pós consulta"),
        (2,"Aguardando formulário pré consulta"),
        (3,"Dieta em andamento"),
        (4,"Dieta concluída"),
    )
    nome=models.CharField(max_length=255)
    email=models.EmailField()
    whatsapp=models.CharField(max_length=11)
    idade = models.IntegerField()
    peso =  models.DecimalField(decimal_places=2, max_digits=6)
    altura = models.DecimalField(decimal_places=2, max_digits=6)
    cpf = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100,blank=True)
    objetivo = models.CharField(max_length=20,blank=True)
    diagnostico = models.BooleanField(default=False)
    status = models.IntegerField(choices=status_paciente,default=1,blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pacientes', blank=True) 