from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import View
from nutricionista.mixins import NutricionistaMixin
from paciente.mixins import PacienteMixin

class Index(NutricionistaMixin, View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Home(NutricionistaMixin, View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AutenticarUsuario(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar-pacientes')
            else:
                return HttpResponse("Usuário ou senha inválidos.")
        else:
            return render(request, self.template_name, {'form': form})

class Logout(NutricionistaMixin, PacienteMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('autenticar-usuario')


