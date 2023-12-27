from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from .models import Alimento
from .forms import AlimentoForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from nutricionista.mixins import NutricionistaMixin
class AlimentoCriar(NutricionistaMixin, CreateView):
    model = Alimento
    form_class = AlimentoForm
    template_name = 'alimento/cadastrarAlimento.html'
    success_url = reverse_lazy('listar-alimentos')
    
class AlimentoListar(NutricionistaMixin, ListView):
    model = Alimento
    template_name = 'alimento/alimentos.html'
    context_object_name = 'alimentos'
    paginate_by = 5
class AlimentoEditar(NutricionistaMixin, UpdateView):
    model = Alimento
    form_class = AlimentoForm
    template_name = 'alimento/editaralimento.html'
    success_url = reverse_lazy('listar-alimentos')
    pk_url_kwarg = 'id'
    
class AlimentoDeletar(NutricionistaMixin, DeleteView):
    model = Alimento
    success_url = reverse_lazy('listar-alimentos')
    pk_url_kwarg = 'id'
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

