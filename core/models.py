from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=30)
    contato = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    class Meta:
        abstract = True
