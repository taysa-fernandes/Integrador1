from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Nutricionista
from .forms import NutricionistaForm
from django.urls import reverse_lazy


class NutricionistaCriar(CreateView):
    model = Nutricionista
    form_class = NutricionistaForm
    template_name = 'core/cadastrar-se.html'
    success_url = reverse_lazy('index') 

def index(request):
    return render(request, 'core/index.html')

def home(request):
    return render(request, 'core/home.html')

