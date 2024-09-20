from .models import Edicao
from django.views.generic import ListView


class ListarEdicoesView(ListView):
    model = Edicao
    template_name = 'JornalDigital/listar_edicoes.html'
    context_object_name = 'edicoes'
    ordering = ['-data']