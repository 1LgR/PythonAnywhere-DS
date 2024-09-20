from django.views.generic import DetailView
from .models import Edicao


class ExibirEdicaoView(DetailView):
    model = Edicao
    template_name = 'JornalDigital/exibir_edicao.html'
    context_object_name = 'edicao'
    pk_url_kwarg = 'edicao_id'