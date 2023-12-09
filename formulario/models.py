from django.db import models

class Pergunta(models.Model):
    TIPOS_FORMULARIO = (
        ('pre', 'Pré-consulta'),
        ('pos', 'Pós-consulta'),
    )

    tipo = models.CharField(max_length=3, choices=TIPOS_FORMULARIO)
    pergunta = models.CharField(max_length=255)
    obrigatorio = models.BooleanField(default=False)

    def __str__(self):
        return self.pergunta

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.TextField()

    def __str__(self):
        return f"Resposta para '{self.pergunta.pergunta}'"
