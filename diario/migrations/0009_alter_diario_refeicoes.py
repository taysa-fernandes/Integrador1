# Generated by Django 4.2.6 on 2023-12-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0004_refeicao_alimentos_delete_alimentorefeicao'),
        ('diario', '0008_remove_diario_refeicoes_do_dia_diario_refeicoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='refeicoes',
            field=models.ManyToManyField(blank=True, related_name='diarios', to='dieta.refeicao'),
        ),
    ]
