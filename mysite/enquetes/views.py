from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta

def index(request):
    lista = Pergunta.objects.all()
    resultado = '<br>'.join(p.texto for p in lista)
    return HttpResponse(
        "<h1>Disciplina:DSweb 2024.1 <br> <h2> 3° período <br><br> Matricula: 20231014040008 <br><br> Aluno: Luiz Gustavo Oliveira Rocha </h2> </h1>"
    )

def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = 'VOTAÇÃO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'RESULTADO da enquente de número %s'
    return HttpResponse(resultado % pergunta_id)