from django.shortcuts import render

def cadastrar_paciente(request):
    return render(request, 'paciente/cadastrarPaciente.html')
