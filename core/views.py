from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')
def dieta(request):
    return render(request, 'core/visualizarDieta.html')
def cadastrar_alimento(request):
    return render(request, 'core/cadastrarAlimento.html')
