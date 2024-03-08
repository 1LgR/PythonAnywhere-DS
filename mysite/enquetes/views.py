from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Disciplina:DSweb 2024.1 <br><br> 3° período <br><br> Matricula: 20231014040008 <br><br> Aluno: Luiz Gustavo Oliveira Rocha</h1>")