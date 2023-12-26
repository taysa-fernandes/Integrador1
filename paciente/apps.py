from django.apps import AppConfig


class PacienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paciente'
    
    def ready(self) -> None:
        from . import signals
        
        return super().ready()
