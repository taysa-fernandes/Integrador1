from django.shortcuts import render

# Create your views here.

def meus_formularios(request):
    return render(request, 'formulario/listar-formularios.html')

def novo_formulario(request):
    return render(request, 'formulario/novo-formulario.html')

def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')