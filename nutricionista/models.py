from django.db import models
from django.conf import settings

class Nutricionista(models.Model):
    nome=models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=11)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nutricionistas')