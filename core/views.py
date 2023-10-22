from django.shortcuts import render

def index(request):
    return render(request, 'core/login.html')

def home(request):
    return render(request, 'core/home.html')

def meus_formularios(request):
    return render(request, 'core/meus-formularios.html')

def novo_formulario(request):
    return render(request, 'core/novo-formulario.html')

def dieta(request):
    return render(request, 'core/visualizarDieta.html')

def progresso(request):
    return render(request, 'core/registrarProgresso.html')

def diario(request):
    return render(request, 'core/diarioAlimentar.html')

def alimentos(request):
    return render(request, 'core/alimentos.html')
