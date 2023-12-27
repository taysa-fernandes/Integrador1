from datetime import timezone
from typing import Any
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy

from nutricionista.models import Nutricionista
from .models import Paciente
from .forms import PacienteForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from nutricionista.mixins import NutricionistaMixin

class PacienteEditar(NutricionistaMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/editarPaciente.html'
    success_url = reverse_lazy('listar-pacientes')
    pk_url_kwarg = 'id'
    
class PacienteDeletar(NutricionistaMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('listar-pacientes')
    pk_url_kwarg = 'id'
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class PacienteCriar(NutricionistaMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/cadastrarPaciente.html'
    success_url = reverse_lazy('listar-pacientes')
    
    def form_valid(self, form):
        # Antes de salvar o formulário, adicionando data de criação
        # form.instance.data_criacao = timezone.now()
        return super().form_valid(form)
    
    
class PacienteListar(NutricionistaMixin, ListView):
    model = Paciente
    template_name = 'core/home.html'
    context_object_name = 'pacientes'
    paginate_by = 3
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:      
        context = super().get_context_data(**kwargs) 
                    
        nutricionista = Nutricionista.objects.get(usuario__id=self.request.user.id)
                
        context['nutricionista'] = nutricionista
                            
        return context
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:      
        context = super().get_context_data(**kwargs) 
                    
        nutricionista = Nutricionista.objects.get(usuario__id=self.request.user.id)
                
        context['nutricionista'] = nutricionista
                            
        return context
    

