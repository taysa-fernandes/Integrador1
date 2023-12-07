from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from .models import Alimento
from .forms import AlimentoForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
  
class AlimentoCriar(CreateView):
    model = Alimento
    form_class = AlimentoForm
    template_name = 'alimento/cadastrarAlimento.html'
    success_url = reverse_lazy('listar-alimentos')
    
class AlimentoListar(ListView):
    model = Alimento
    template_name = 'alimento/alimentos.html'
    context_object_name = 'alimentos'

