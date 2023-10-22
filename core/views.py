from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def meus_formularios(request):
    return render(request, 'core/meus-formularios.html')

def novo_formulario(request):
    return render(request, 'core/novo-formulario.html')

def dieta(request):
    return render(request, 'core/visualizarDieta.html')
