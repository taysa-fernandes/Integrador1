from django.db import models

class Resposta(models.Model):
    opcao = models.IntegerField()
    id_pergunta = models.IntegerField()
    
