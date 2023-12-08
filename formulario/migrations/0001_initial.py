# Generated by Django 4.2.6 on 2023-12-07 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('pre', 'Pré-consulta'), ('pos', 'Pós-consulta')], max_length=3)),
                ('pergunta', models.CharField(max_length=255)),
                ('obrigatorio', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField()),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.pergunta')),
            ],
        ),
    ]