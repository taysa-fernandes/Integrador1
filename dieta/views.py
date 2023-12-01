from django.shortcuts import render

# Create your views here.

def cadastrar_dieta(request):
    return render(request, 'dieta/cadastrar-dieta.html')


def dieta(request):
    return render(request, 'dieta/visualizar-dieta.html')
