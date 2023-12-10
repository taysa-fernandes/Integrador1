from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from alimento.models import Alimento
from .models import Refeicao, Dieta, AlimentoRefeicao
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

# Create your views here.

class CadastrarDieta(View):
    template_name = 'dieta/cadastrar-dieta.html' 
    
    def post(self, request):
        dados_formulario = request.POST
        
        for refeicao in Refeicao.objects.all():
                nome_opcao = f'opcao_{refeicao.id}'
                nome_substituto = f'substituto_{refeicao.id}'

                opcao_selecionada = dados_formulario.get(nome_opcao)
                substituto_selecionado = dados_formulario.get(nome_substituto)

                # opção e substituto foram selecionados
                if opcao_selecionada and substituto_selecionado:
                    alimento_opcao = Alimento.objects.get(nome=opcao_selecionada)
                    alimento_substituto = Alimento.objects.get(nome=substituto_selecionado)

                    AlimentoRefeicao.objects.create(alimento=alimento_opcao, refeicao=refeicao)
                    AlimentoRefeicao.objects.create(alimento=alimento_substituto, refeicao=refeicao)
            
            
        return redirect('listar-dietas')


class ListarDietas(ListView):
    model = Dieta
    template_name = 'dieta/listar-dietas.html'
    context_object_name = 'dietas'
    
class DefinirNumeroRefeicoes(View):
    template_name = 'dieta/definir-numero-refeicoes.html'  # Adjust the template name as needed
    success_url = 'cadastrar-dieta'  # Adjust the success URL as needed

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        numero_refeicoes = request.POST.get('numero-refeicoes')
        nome_dieta = request.POST.get('nome-dieta')

        if numero_refeicoes and nome_dieta:
            numero_refeicoes_int = range(1, int(numero_refeicoes) + 1)
            dieta = Dieta.objects.create(nome=nome_dieta)
            refeicoes = [Refeicao.objects.create(nome=f'Refeição {num_refeicao}', dieta=dieta)
                         for num_refeicao in numero_refeicoes_int]
            alimentos = Alimento.objects.all()

            context = {
                'refeicoes': refeicoes,
                'alimentos': alimentos,
            }

            return render(request, 'dieta/cadastrar-dieta.html', context)

        return render(request, self.template_name)

def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')
