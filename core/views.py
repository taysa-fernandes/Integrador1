from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def dieta(request):
    return render(request, 'core/visualizar-dieta.html')

def progresso(request):
    return render(request, 'core/registrar-progresso.html')

def diario(request):
    return render(request, 'core/diario-alimentar.html')

def home(request):
    return render(request, 'core/home.html')

def meus_formularios(request):
    return render(request, 'core/meus-formularios.html')

def novo_formulario(request):
    return render(request, 'core/novo-formulario.html')

def alimentos(request):
    return render(request, 'core/alimentos.html')
