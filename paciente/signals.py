from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import Paciente

@receiver(signal=pre_save, sender=Paciente)
def create_person_auth_user(sender, instance: Paciente, **kwargs):
    with transaction.atomic():
        User = get_user_model()
        try:
            auth_user = User.objects.get(username=instance.email)
            auth_user.username = instance.email
            auth_user.set_password(instance.cpf)
            auth_user.save()
        except User.DoesNotExist:
            auth_user = User.objects.create_user(username=instance.email, password=instance.cpf)
            grupo_pacientes = Group.objects.get(name='PACIENTES')
            auth_user.groups.add(grupo_pacientes)
            auth_user.save()
            instance.usuario = auth_user