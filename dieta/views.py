from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from alimento.models import Alimento
from .models import Refeicao, Dieta
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .forms import DietaForm

# Create your views here.

class CadastrarDieta(View):
    template_name_create = 'dieta/cadastrar-dieta.html' 
    template_name_process = 'dieta/definir-numero-refeicoes.html'

    def get(self, request, *args, **kwargs):
        return redirect('definir-numero-refeicoes')
    
    def post(self, request, *args, **kwargs):
        dados_formulario = request.POST
        dieta_id = dados_formulario.get('dieta_id')
        
        if dieta_id is None:
            # Lógica para criar a dieta
            numero_refeicoes = dados_formulario.get('numero-refeicoes')
            nome_dieta = dados_formulario.get('nome-dieta')

            if numero_refeicoes and nome_dieta:
                numero_refeicoes_int = range(1, int(numero_refeicoes) + 1)            
                dieta = Dieta.objects.create(nome=nome_dieta)
                refeicoes = [Refeicao.objects.create(nome=f'Refeição {num_refeicao}', dieta=dieta)
                             for num_refeicao in numero_refeicoes_int]
                alimentos = Alimento.objects.all()

                context = {
                    'refeicoes': refeicoes,
                    'alimentos': alimentos,
                    'dieta': dieta
                }

                return render(request, self.template_name_create, context)
            
        dieta = get_object_or_404(Dieta, id=dieta_id)
        # Lógica para processar o formulário da dieta existente
        for refeicao in dieta.refeicoes.all():
            nome_opcao = f'opcao_{refeicao.id}'
            nome_substituto = f'substituto_{refeicao.id}'
            
            print('dados do formulario de criar: ', dados_formulario)
            
            opcao_selecionada = dados_formulario.get(nome_opcao)
            substituto_selecionado = dados_formulario.get(nome_substituto)

            # opção e substituto foram selecionados
            if opcao_selecionada and substituto_selecionado:
                alimento_opcao = Alimento.objects.get(nome=opcao_selecionada)
                alimento_substituto = Alimento.objects.get(nome=substituto_selecionado)

                refeicao.alimentos.set([alimento_opcao, alimento_substituto])

        return redirect('listar-dietas')


class ListarDietas(ListView):
    model = Dieta
    template_name = 'dieta/listar-dietas.html'
    context_object_name = 'dietas'
    
class DefinirNumeroRefeicoes(View):
    template_name = 'dieta/definir-numero-refeicoes.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class EditarDieta(UpdateView):
    model = Dieta
    template_name = 'dieta/editar-dieta.html'
    form_class = DietaForm 
    pk_url_kwarg = 'dieta_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dieta = self.get_object()
        
        alimentos_do_sistema = Alimento.objects.all()
          
        context['dieta'] = dieta
        
        refeicoes_da_dieta = dieta.refeicoes.all()
                
        informacoes_das_refeicoes = []
        
        for refeicao in refeicoes_da_dieta:
            alimentos_da_refeicao = refeicao.alimentos.all()
            
            informacoes_das_refeicoes.append({
                'refeicao': refeicao,
                'alimentos': alimentos_do_sistema,
            })  
        
        context['informacoes_refeicoes'] = informacoes_das_refeicoes        

        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        dados_formulario = request.POST
        dieta_id = dados_formulario.get('dieta_id')
        dieta = get_object_or_404(Dieta, id=dieta_id)
        print('dados do form de edit: ', dados_formulario)
        # Lógica para processar o formulário da dieta existente
        for refeicao in dieta.refeicoes.all():
            nome_opcao = f'opcao_{refeicao.id}'
            nome_substituto = f'substituto_{refeicao.id}'
            
            opcao_selecionada = dados_formulario.get(nome_opcao)
            substituto_selecionado = dados_formulario.get(nome_substituto)

            # opção e substituto foram selecionados
            if opcao_selecionada and substituto_selecionado:
                alimento_opcao = Alimento.objects.get(nome=opcao_selecionada)
                alimento_substituto = Alimento.objects.get(nome=substituto_selecionado)

                refeicao.alimentos.set([alimento_opcao, alimento_substituto])

        return redirect('listar-dietas')
            
    def get_success_url(self):
        return reverse_lazy('listar-dietas') 

def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')

class DeletarDieta(DeleteView):
    model = Dieta
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listar-dietas') 
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Chame o método delete diretamente
        return self.delete(request, *args, **kwargs)