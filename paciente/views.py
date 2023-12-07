from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

class PacienteEditar(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/cadastrarPaciente.html'
    success_url = reverse_lazy('core/home.html')
    pk_url_kwarg = 'id'
    
class PacienteDeletar(DeleteView):
    model = Paciente
    success_url = reverse_lazy('core/home.html')
    pk_url_kwarg = 'id'
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class PacienteCriar(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/cadastrarPaciente.html'
    success_url = reverse_lazy('listar-pacientes')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    
class PacienteListar(ListView):
    model = Paciente
    template_name = 'core/home.html'
    context_object_name = 'pacientes'
    
    def get(self, request, *args, **kwargs):
        print("Entrou no método get")  # Adicione esta linha para verificar se o método está sendo chamado
        response = super().get(request, *args, **kwargs)
        
        # Imprima os pacientes
        pacientes = self.object_list
        print("Pacientes:", pacientes)

        return response

