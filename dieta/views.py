from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from alimento.models import Alimento
from .models import Refeicao, Dieta
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

# Create your views here.

class CadastrarDieta(View):
    # template_name = 'dieta/cadastrar-dieta.html' 
    
    def post(self, request):
        dados_formulario = request.POST
        dieta_id = dados_formulario.get('dieta_id')
        dieta = get_object_or_404(Dieta, id=dieta_id)
        
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


class ListarDietas(ListView):
    model = Dieta
    template_name = 'dieta/listar-dietas.html'
    context_object_name = 'dietas'
    
class DefinirNumeroRefeicoes(View):
    template_name = 'dieta/definir-numero-refeicoes.html' 
    success_url = 'cadastrar-dieta'

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
                'dieta': dieta
            }

            return render(request, 'dieta/cadastrar-dieta.html', context)

        return render(request, self.template_name)

class EditarDieta(UpdateView):
    model = Refeicao
    template_name = 'dieta/cadastrar-dieta.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('listar-dietas') 

def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')

class DeletarDieta(DeleteView):
    model = Dieta
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listar-dietas') 