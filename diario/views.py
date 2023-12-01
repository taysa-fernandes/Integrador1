from django.shortcuts import render

# Create your views here.
def diario(request):
    return render(request, 'diario/diarioAlimentar.html')
