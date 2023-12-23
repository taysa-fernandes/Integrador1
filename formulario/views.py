from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Formulario, Pergunta
from .forms import FormularioForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# Create your views here.

class DefinirNumeroQuestoes(View):
    template_name = 'formulario/definir-numero-questoes.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CriarFormulario(View):
    template_name_create = 'formulario/criar-formulario.html' 
    template_name_process = 'formulario/definir-numero-questoes.html'

    def get(self, request, *args, **kwargs):
        return redirect('definir-numero-questoes')
    
    def post(self, request, *args, **kwargs):
        dados_formulario = request.POST
        formulario_id = dados_formulario.get('formulario_id')
        
        if formulario_id is None:
            # Lógica para criar formulário
            nome_formulario = dados_formulario.get('nome-formulario')
            numero_questoes = dados_formulario.get('numero-questoes')

            if nome_formulario and numero_questoes:
                numero_questoes_int = range(1, int(numero_questoes) + 1)            
                formulario = Formulario.objects.create(nome=nome_formulario)
                questoes = [Pergunta.objects.create(nome=f'Pergunta {num_questao}', formulario=formulario)
                             for num_questao in numero_questoes_int]
                
                context = {
                    'questoes': questoes,
                    'formulario': formulario,
                }

                return render(request, self.template_name_create, context)
            
        formulario = get_object_or_404(Formulario, id=formulario_id)
        
        perguntas_do_forms = formulario.perguntas.all()
        # Lógica para processar o formulário existente
        for pergunta in perguntas_do_forms:
            nome_pergunta = f'pergunta_{pergunta.id}'
                                                
            nome_pergunta_inserida = dados_formulario.get(nome_pergunta)
        
            if nome_pergunta_inserida:                
                pergunta.pergunta = nome_pergunta_inserida
                                
                pergunta.save()

        return redirect('listar-formularios')

class ListarFormularios(ListView):
    model = Formulario
    template_name = 'formulario/listar-formularios.html'
    context_object_name = 'formularios'
    
class EditarFormulario(UpdateView):
    model = Formulario
    template_name = 'formulario/editar-formulario.html'
    form_class = FormularioForm 
    pk_url_kwarg = 'formulario_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formulario = self.get_object()
                  
        context['formulario'] = formulario
        
        perguntas_do_forms = formulario.perguntas.all()
                                                
        context['questoes'] = perguntas_do_forms

        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        dados_formulario = request.POST
        formulario_id = dados_formulario.get('formulario_id')
        formulario = get_object_or_404(Formulario, id=formulario_id)
        
        perguntas_do_forms = formulario.perguntas.all()
        
        for pergunta in perguntas_do_forms:
            nome_pergunta = f'pergunta_{pergunta.id}'
                                                
            nome_pergunta_inserida = dados_formulario.get(nome_pergunta)
        
            if nome_pergunta_inserida:                
                pergunta.pergunta = nome_pergunta_inserida
                                
                pergunta.save()

        return redirect('listar-formularios')
            
    def get_success_url(self):
        return reverse_lazy('listar-dietas') 
    
class DeletarFormulario(DeleteView):
    model = Formulario
    pk_url_kwarg = 'formulario_id'
    success_url = reverse_lazy('listar-formularios') 
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Chame o método delete diretamente
        return self.delete(request, *args, **kwargs)