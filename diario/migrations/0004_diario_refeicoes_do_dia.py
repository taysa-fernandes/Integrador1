# Generated by Django 4.2.6 on 2023-12-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0003_alter_diario_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='diario',
            name='refeicoes_do_dia',
            field=models.JSONField(default=list),
        ),
    ]
