from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Formulario, Pergunta
# Create your views here.

class DefinirNumeroQuestoes(View):
    template_name = 'formulario/definir-numero-questoes.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CriarFormulario(View):
    template_name_create = 'formulario/criar-formulario.html' 
    template_name_process = 'formulario/definir-numero-questoes.html'

    def get(self, request, *args, **kwargs):
        return redirect('definir-numero-questoes')
    
    def post(self, request, *args, **kwargs):
        dados_formulario = request.POST
        formulario_id = dados_formulario.get('formulario_id')
        
        if formulario_id is None:
            # Lógica para criar formulário
            nome_formulario = dados_formulario.get('nome-formulario')
            numero_questoes = dados_formulario.get('numero-questoes')

            if nome_formulario and numero_questoes:
                numero_questoes_int = range(1, int(numero_questoes) + 1)            
                formulario = Formulario.objects.create(nome=nome_formulario)
                questoes = [Pergunta.objects.create(nome=f'Pergunta {num_questao}', formulario=formulario)
                             for num_questao in numero_questoes_int]
                
                context = {
                    'questoes': questoes,
                    'formulario': formulario,
                }

                return render(request, self.template_name_create, context)
            
        formulario = get_object_or_404(Formulario, id=formulario_id)
        
        perguntas_do_forms = formulario.perguntas.all()
        # Lógica para processar o formulário existente
        for pergunta in perguntas_do_forms:
            nome_pergunta = f'pergunta_{pergunta.id}'
                                                
            nome_pergunta_inserida = dados_formulario.get(nome_pergunta)
        
            if nome_pergunta_inserida:                
                pergunta.pergunta = nome_pergunta_inserida
                
                pergunta.save()

        return redirect('listar-formularios')

def meus_formularios(request):
    return render(request, 'formulario/listar-formularios.html')

def novo_formulario(request):
    return render(request, 'formulario/criar-formulario.html')

def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')