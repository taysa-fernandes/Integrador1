# Generated by Django 4.2.6 on 2023-12-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0004_diario_refeicoes_do_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='data',
            field=models.DateTimeField(editable=False),
        ),
    ]