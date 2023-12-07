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
    
# def lista_pacientes(request):
#     pacientes = Paciente.objects.all() 
#     return render(request, 'core/home.html', {'pacientes': pacientes})
    
class PacienteListar(ListView):
    model = Paciente
    template_name = 'core/home.html'
    context_object_name = 'pacientes'
    

