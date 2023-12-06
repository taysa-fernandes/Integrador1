from django.db import models


class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    porcao = models.DecimalField(decimal_places=2, max_digits=6)
    valor_energetico = models.DecimalField(decimal_places=2, max_digits=6)
    fibra_alimentar = models.DecimalField(decimal_places=2, max_digits=6)
    carboidratos = models.DecimalField(decimal_places=2, max_digits=6)
    proteinas = models.DecimalField(decimal_places=2, max_digits=6)
    gorduras = models.DecimalField(decimal_places=2, max_digits=6)
    e_substituto = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
