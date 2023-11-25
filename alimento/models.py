from django.db import models


class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    porcao = models.DecimalField(max_digits=6, decimal_places=6)
    valor_energetico = models.DecimalField(max_digits=6, decimal_places=6)
    fibra_alimentar = models.DecimalField(max_digits=6, decimal_places=6)
    carboidratos = models.DecimalField(max_digits=6, decimal_places=6)
    proteinas = models.DecimalField(max_digits=6, decimal_places=6)
    gorduras = models.DecimalField(max_digits=6, decimal_places=6)
    e_substituto = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
