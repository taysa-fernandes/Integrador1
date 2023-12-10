from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Pergunta,Resposta,Formulario
from .forms import PerguntaForm,RespostaForm
from django.urls import reverse_lazy

# def meus_formularios(request):
#     return render(request, 'formulario/meus-formularios.html')

# def novo_formulario(request):
#     return render(request, 'formulario/novo-formulario.html')
class FormularioCriar(CreateView):
    model = Formulario
    template_name = 'formulario/novo-formulario.html'
    form_class = PerguntaForm
    success_url = reverse_lazy('listar-formularios')

    def form_valid(self, form):
        formulario = form.save()  # Salva o formulário principal

        perguntas = self.request.POST.getlist('pergunta')
        for pergunta_texto in perguntas:
            pergunta = Pergunta(pergunta=pergunta_texto, formulario=formulario)
            pergunta.save()

        return super().form_valid(form)
class FormularioListar(ListView):
    model = Pergunta
    template_name = 'formulario/meus-formularios.html'
    context_object_name = 'formularios'
    
def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')