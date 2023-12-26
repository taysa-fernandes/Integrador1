from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from datetime import datetime
import locale
from .forms import DiarioForm
from paciente.models import Paciente
from dieta.models import Dieta
from django.urls import reverse_lazy
from .models import Diario
from django.core.serializers import serialize
# from django.contrib.messages.views import SuccessMessageMixin
from paciente.mixins import PacienteMixin
from nutricionista.mixins import NutricionistaMixin

locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

# Create your views here.
class CriarDiario(PacienteMixin, View):
    
    def get(self, request): 

        data_atual = datetime.now()
        
        dia_do_mes = data_atual.day
        mes = data_atual.strftime("%B").capitalize()  # Nome do mês em português
        dia_da_semana = data_atual.strftime("%A").capitalize().replace("-feira", "")  # Dia da semana em português
        ano_atual = data_atual.year
        
        data_especifica = datetime(ano_atual, data_atual.month, dia_do_mes) 
        diario_do_dia = Diario.objects.filter(data__date=data_especifica)
        
        
        if not diario_do_dia.exists():
            
            paciente = get_object_or_404(Paciente, usuario=request.user)
            
            print('encontrei paciente', paciente)
            
            dieta_do_dia = paciente.dietas.filter(status='andamento').first()
            
            print("dieta do dia: ", dieta_do_dia)
            print("refeições da dieta: ", dieta_do_dia.refeicoes.all())
            
            novo_diario = Diario.objects.create(data=data_atual, paciente=paciente)
            
            # novo_diario.paciente = paciente
            
            refeicoes_serializadas = serialize('json', dieta_do_dia.refeicoes.all())
            novo_diario.refeicoes = refeicoes_serializadas
            
            novo_diario.save()
            
        return redirect('listar-diarios')
    
class RegistrarProgressoNoDiario(PacienteMixin, CreateView):
    template_name = 'diario/registrarProgresso.html'
    form_class = DiarioForm
    success_url = reverse_lazy('diario')
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['diario'] = self.kwargs.get('id')  # id_diário está nos parâmetros da URL
         
        return context
    
class AtualizarDiario(PacienteMixin, NutricionistaMixin,  UpdateView):
    model = Diario
    form_class = DiarioForm
    template_name = 'diario/registrarProgresso.html'
    success_url = reverse_lazy('listar-diarios')
    pk_url_kwarg = 'id'
    # success_message = 'Diário registrado!'s
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:      
        context = super().get_context_data(**kwargs) 
                    
        paciente = Paciente.objects.get(usuario__id=self.request.user.id)
        
        diario_id = self.kwargs.get(self.pk_url_kwarg)
        diario = Diario.objects.get(id=diario_id)
        
        context['dieta'] = paciente.dietas.filter(status='andamento').first()
        
        context['refeicoes'] = diario.refeicoes.all()
        
        print('alimentos aqui: ', self.get_object().alimentos.all())
                    
        return context
    
class ListarDiarios(PacienteMixin, ListView):
    model = Diario
    template_name = 'paciente/home-paciente.html'
    context_object_name = 'diarios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        paciente = get_object_or_404(Paciente, usuario=self.request.user)
        
        print('aaaaaaaaaaa: ', paciente)
                
        context['paciente'] = paciente

        return context