from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def home(request):
    return render(request, 'core/home.html')

def meus_formularios(request):
    return render(request, 'core/meus-formularios.html')

def novo_formulario(request):
    return render(request, 'core/novo-formulario.html')

def dieta(request):
    return render(request, 'core/visualizarDieta.html')

def cadastrar_alimento(request):
    return render(request, 'core/cadastrarAlimento.html')

def alimentos(request):
    return render(request, 'core/alimentos.html')

def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')

def cadastrar_paciente(request):
    return render(request, 'core/cadastrarPaciente.html')
