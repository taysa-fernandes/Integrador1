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
    paginate_by = 3 

    def get(self, request, *args, **kwargs):
        # Obter o valor do parâmetro 'tipo' da URL ou usar 'comuns' como padrão
        tipo_alimento = self.request.GET.get('tipo', 'comuns')

        # Validar o valor do parâmetro, se necessário
        # Você pode adicionar lógica para garantir que o valor seja válido

        # Armazenar o valor na instância da classe para que ele possa ser usado em outros métodos
        self.tipo_alimento = tipo_alimento

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # Filtrar os alimentos com base no valor do parâmetro 'tipo'
        if self.tipo_alimento == 'substitutos':
            return Alimento.objects.filter(e_substituto=True)
        else: 
            return Alimento.objects.filter(e_substituto=False)
        
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

