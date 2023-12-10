from django.db import models

class Formulario(models.Model):
    TIPOS_FORMULARIO = (
        ('pre-consulta', 'Pré-consulta'),
        ('pos-consulta', 'Pós-consulta'),
    )

    tipo = models.CharField(max_length=15, choices=TIPOS_FORMULARIO, default='pre-consulta')

    def __str__(self):
        return f"Formulário {self.id} - {self.tipo}"


class Pergunta(models.Model):
    formulario = models.ForeignKey(Formulario, related_name='perguntas', on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=255)
    obrigatorio = models.BooleanField(default=False)

    def __str__(self):
        return self.pergunta

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.TextField()

    def __str__(self):
        return f"Resposta para '{self.pergunta.pergunta}'"
