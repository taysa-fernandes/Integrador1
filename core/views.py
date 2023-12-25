from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    return render(request, 'core/index.html')

def home(request):
    return render(request, 'core/home.html')

def autenticar_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print('form is valid!')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar-pacientes')
            else:
                # Retorne uma mensagem de erro.
                return HttpResponse("Usuário ou senha inválidos.")
        else: 
            print('form invalido!')
    else:
        form = AuthenticationForm()

    return render(request, 'core/index.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('autenticar-usuario')
