from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')
def diario(request):
    return render(request, 'core/visualizarDieta.html')
