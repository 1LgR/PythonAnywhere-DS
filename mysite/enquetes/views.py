from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    enquetes = Pergunta.objects.order_by('-data_pub')
    contexto = {'lista_enquetes': enquetes}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

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

"""