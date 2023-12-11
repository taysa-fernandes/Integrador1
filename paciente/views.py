from datetime import timezone
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

class PacienteEditar(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/editarPaciente.html'
    success_url = reverse_lazy('listar-pacientes')
    pk_url_kwarg = 'id'
    
class PacienteDeletar(DeleteView):
    model = Paciente
    success_url = reverse_lazy('listar-pacientes')
    pk_url_kwarg = 'id'
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class PacienteCriar(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/cadastrarPaciente.html'
    success_url = reverse_lazy('listar-pacientes')
    
    def form_valid(self, form):
        # Antes de salvar o formulário, adicionando data de criação
        # form.instance.data_criacao = timezone.now()
        return super().form_valid(form)
    
    
class PacienteListar(ListView):
    model = Paciente
    template_name = 'core/home.html'
    context_object_name = 'pacientes'
    

