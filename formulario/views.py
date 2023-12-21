from django.shortcuts import render, redirect
from django.views import View
# Create your views here.

class DefinirNumeroQuestoes(View):
    template_name = 'formulario/definir-numero-questoes.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CriarFormulario(View):
    template_name_create = 'dieta/criar-formulario.html' 
    template_name_process = 'dieta/definir-numero-questoes.html'

    def get(self, request, *args, **kwargs):
        return redirect('definir-numero-questoes')
    
    def post(self, request, *args, **kwargs):
        dados_formulario = request.POST
        formulario_id = dados_formulario.get('formulario_id')
        
        if formulario_id is None:
            # Lógica para criar a dieta
            numero_questoes = dados_formulario.get('numero-refeicoes')
            nome_dieta = dados_formulario.get('nome-dieta')

            if numero_questoes and nome_dieta:
                numero_questoes_int = range(1, int(numero_questoes) + 1)            
                dieta = Dieta.objects.create(nome=nome_dieta)
                refeicoes = [Refeicao.objects.create(nome=f'Refeição {num_refeicao}', dieta=dieta)
                             for num_refeicao in numero_questoes_int]
                alimentos = Alimento.objects.all()

                context = {
                    'refeicoes': refeicoes,
                    'alimentos': alimentos,
                    'dieta': dieta
                }

                return render(request, self.template_name_create, context)
            
        dieta = get_object_or_404(Dieta, id=dieta_id)
        # Lógica para processar o formulário da dieta existente
        for refeicao in dieta.refeicoes.all():
            nome_opcao = f'opcao_{refeicao.id}'
            nome_substituto = f'substituto_{refeicao.id}'
            
            print('dados do formulario de criar: ', dados_formulario)
            
            opcao_selecionada = dados_formulario.get(nome_opcao)
            substituto_selecionado = dados_formulario.get(nome_substituto)

            # opção e substituto foram selecionados
            if opcao_selecionada and substituto_selecionado:
                alimento_opcao = Alimento.objects.get(nome=opcao_selecionada)
                alimento_substituto = Alimento.objects.get(nome=substituto_selecionado)

                refeicao.alimentos.set([alimento_opcao, alimento_substituto])

        return redirect('listar-dietas')

def meus_formularios(request):
    return render(request, 'formulario/listar-formularios.html')



def novo_formulario(request):
    return render(request, 'formulario/novo-formulario.html')

def tipo_questao(request):
    return render(request, 'core/tipo-questao.html')