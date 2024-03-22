from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'enquetes/detalhes.html', contexto)

def votacao(request, pergunta_id):
    resultado = 'VOTAÇÃO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'RESULTADO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

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