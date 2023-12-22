from django.db import models
from enum import Enum

class TipoFormulario(Enum):
    PRE_CONSULTA = 'Pré consulta'
    POS_CONSULTA = 'Pós consulta'

class TipoPergunta(Enum):
    PERGUNTA_ABERTA = 'Pergunta aberta'

class Formulario(models.Model):
    tipo = [(tipo.name, tipo.value) for tipo in TipoFormulario]
    nome = models.CharField(max_length=255)
    
class Pergunta(models.Model):
    nome=models.CharField(max_length=255)
    tipo_pergunta = [(tipo.name, tipo.value) for tipo in TipoPergunta]
    e_obrigatoria = models.BooleanField(default=False)
    pergunta = models.CharField(max_length=255)
    resposta = models.TextField(blank=True)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='perguntas')