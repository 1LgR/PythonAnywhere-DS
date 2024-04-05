from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Alternativa

def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
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
        return HttpResponseRedirect(reverse(
            'enquetes:resultado', args=(pergunta.id,)
        ))

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/resultado.html', contexto)


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

"""