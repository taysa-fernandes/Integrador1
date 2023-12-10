from django.shortcuts import render
from django.views import View
from datetime import datetime
import locale

# Create your views here.
class Diario(View):
    
    def get(self, request): 
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

        data_atual = datetime.now()

        dia_do_mes = data_atual.day
        mes = data_atual.strftime("%B").capitalize()  # Nome do mês em português
        dia_da_semana = data_atual.strftime("%A").capitalize()  # Dia da semana em português

        context = {
            'dia_do_mes': dia_do_mes,
            'mes': mes,
            'dia_da_semana': dia_da_semana,
        }

        return render(request, 'diario/diarioAlimentar.html', context)
