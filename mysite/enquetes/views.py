from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Alternativa
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista = Pergunta.objects.order_by('-data_pub')
        contexto = {'lista_enquetes': lista}
        return render(request, 'enquetes/index.html', contexto)

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        enquete = get_object_or_404(Pergunta, pk=pergunta_id)
        return render(request, 'enquetes/detalhes.html', {'pergunta': enquete})

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        id_alternativa = request.POST.get('escolha')  # Usa get para evitar KeyError

        if not id_alternativa:  # Verifica se id_alternativa está vazio
            contexto = {
                'pergunta': pergunta,
                'error': 'Você precisa selecionar uma alternativa.'
            }
            return render(request, 'enquetes/detalhes.html', contexto)

        try:
            alt = pergunta.alternativa_set.get(pk=id_alternativa)
        except Alternativa.DoesNotExist:
            contexto = {
                'pergunta': pergunta,
                'error': 'Alternativa inválida.'
            }
            return render(request, 'enquetes/detalhes.html', contexto)
        else:
            alt.quant_votos += 1
            alt.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        enquete = get_object_or_404(Pergunta, pk=pergunta_id)
        return render(request, 'enquetes/resultado.html', {'pergunta': enquete})



####
## Histórico de Versões
"""
--> View INDEX - Versão 1
def index(request):
    enquetes = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    contexto = {'lista_enquetes': enquetes}
    return HttpResponse(template.render(contexto, request))

--> View DETALHES - Versão 1
def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/resultado.html', contexto)



class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        enquete = get_object_or_404(Pergunta, pk=pergunta_id)
        return render(request, 'enquetes/detalhes.html', {'pergunta': enquete})

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        try:
            id_alternativa = request.POST['escolha']
            alt = pergunta.alternativa_set.get(pk=id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'enquete': pergunta,
                'error': 'Você precisa selecionar uma alternativa.'
            }
            return render(request, 'enquetes/detalhes.html', contexto)
        else:
            alt.quant_votos += 1
            alt.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))
"""