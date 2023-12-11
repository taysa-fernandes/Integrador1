# Generated by Django 4.2.6 on 2023-12-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimento', '0003_remove_alimento_valor_energetico_alimento_calorias_and_more'),
        ('dieta', '0003_dieta_paciente_alter_dieta_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='refeicao',
            name='alimentos',
            field=models.ManyToManyField(related_name='refeicoes', to='alimento.alimento'),
        ),
        migrations.DeleteModel(
            name='AlimentoRefeicao',
        ),
    ]
