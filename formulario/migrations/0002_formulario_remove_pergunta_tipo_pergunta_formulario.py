# Generated by Django 4.2.6 on 2023-12-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('pre-consulta', 'Pré-consulta'), ('pos-consulta', 'Pós-consulta')], default='pre-consulta', max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='tipo',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='formulario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='formulario.formulario'),
        ),
    ]
