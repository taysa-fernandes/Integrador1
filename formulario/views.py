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
        
        print('formulario entrou no chat: ', dados_formulario)
        print('id do formulario: ', formulario_id)
        
        if formulario_id is None:
            # Lógica para criar formulário
            nome_formulario = dados_formulario.get('nome-formulario')
            numero_questoes = dados_formulario.get('numero-questoes')

            if nome_formulario and numero_questoes:
                numero_questoes_int = range(1, int(numero_questoes) + 1)            
                formulario = Formulario.objects.create(nome=nome_formulario)
                questoes = [Pergunta.objects.create(pergunta=f'Pergunta {num_questao}', formulario=formulario)
                             for num_questao in numero_questoes_int]
                
                print('formulario criado: ', formulario)
                # print('perguntas criadas: ', questoes)

                context = {
                    # 'questoes': questoes,
                    'formulario': formulario,
                }

                return render(request, self.template_name_create, context)
            
        formulario = get_object_or_404(Formulario, id=formulario_id)
        # Lógica para processar o formulário existente
        print('formulario existe: ', formulario)
        # for pergunta in formulario.perguntas.all():
        #     nome_pergunta = f'pergunta_{{questao.id}}'
        #     nome_resposta = f'resposta_{{questao.id}}'
            
        #     print('dados do formulario de criar: ', dados_formulario)
            
        #     nome_pergunta_do_formulario = dados_formulario.get(nome_pergunta)
        #     nome_resposta_do_formulario = dados_formulario.get(nome_resposta)

        #     if nome_pergunta_do_formulario:
        #         pergunta = Pergunta.objects.get(nome=nome_pergunta_do_formulario)
        #         resposta = Pergunta.objects.get(nome=nome_resposta_do_formulario)

        #         refeicao.alimentos.set([alimento_opcao, alimento_substituto])

        return redirect('listar-formularios')

def meus_formularios(request):
    return render(request, 'formulario/listar-formularios.html')

def novo_formulario(request):
    return render(request, 'formulario/criar-formulario.html')

def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')