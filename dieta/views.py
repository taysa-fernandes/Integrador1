from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from alimento.models import Alimento


# Create your views here.

def cadastrar_dieta(request):
    numero_refeicoes = request.GET.get('numero_refeicoes', None)
    numero_opcoes = request.GET.get('numero_opcoes', None)
    
    context = {
        'numero_refeicoes': numero_refeicoes,
        'numero_opcoes': numero_opcoes
    }
    
    return render(request, 'dieta/cadastrar-dieta.html', context)


def listar_dietas(request): 
    return render(request, 'dieta/listar-dietas.html')
    
    
def definir_numero_refeicoes(request): 
    if request.method == 'POST':
        numero_refeicoes = request.POST.get('numero-refeicoes')
        alimentos = Alimento.objects.all()
        
        context = {
            'numero_refeicoes': numero_refeicoes,
            'alimentos': alimentos,
        }
        
        return render(request, 'dieta/definir-numero-refeicoes.html', context)
    
    return render(request, 'dieta/definir-numero-refeicoes.html')

def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')
