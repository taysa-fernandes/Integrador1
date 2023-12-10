from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from alimento.models import Alimento
from .models import Refeicao, Dieta, AlimentoRefeicao
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

# Create your views here.

def cadastrar_dieta(request):
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


def listar_dietas(request): 
    dietas = Dieta.objects.all()
    
    return render(request, 'dieta/listar-dietas.html', { 'dietas': dietas })
    
    
def definir_numero_refeicoes(request): 
    if request.method == 'POST':
        numero_refeicoes = request.POST.get('numero-refeicoes')
        numero_refeicoes_int = range(1, int(numero_refeicoes) + 1)
        nome_dieta = request.POST.get('nome-dieta')
        
        dieta = Dieta.objects.create(nome=nome_dieta)
        
        refeicoes = []
        
        for num_refeicao in numero_refeicoes_int:
            refeicao = Refeicao.objects.create(nome=f'Refeição {num_refeicao}', dieta=dieta)
            refeicoes.append(refeicao)
            
        alimentos = Alimento.objects.all()
        
        context = {
            'refeicoes': refeicoes,
            'alimentos': alimentos,
        }
        
        return render(request, 'dieta/cadastrar-dieta.html', context)
    
    return render(request, 'dieta/definir-numero-refeicoes.html')

def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')
