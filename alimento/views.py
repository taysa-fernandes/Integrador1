from django.shortcuts import render

# Create your views here.
def cadastrar_alimento(request):
    return render(request, 'alimento/cadastrarAlimento.html')

def alimentos(request):
    return render(request, 'alimento/alimentos.html')

