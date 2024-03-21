from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta
from django.template import loader

def index(request):
    enquetes = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    contexto = {'lista_enquetes': enquetes}
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = 'VOTAÇÃO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'RESULTADO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)