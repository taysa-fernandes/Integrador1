from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Pergunta,Resposta
from .forms import PerguntaForm,RespostaForm
from django.urls import reverse_lazy

# def meus_formularios(request):
#     return render(request, 'formulario/meus-formularios.html')

# def novo_formulario(request):
#     return render(request, 'formulario/novo-formulario.html')
class FormularioCriar(CreateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'formulario/novo-formulario.html'
    success_url = reverse_lazy('listar-formularios')
class FormularioListar(ListView):
    model = Pergunta
    template_name = 'formulario/meus-formularios.html'
    context_object_name = 'formularios'
    
def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')