from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edicao
from .forms import EdicaoForm


class CadastrarEdicaoView(LoginRequiredMixin, CreateView):
    model = Edicao
    form_class = EdicaoForm
    template_name = 'JornalDigital/cadastrar_edicao.html'

    def form_valid(self, form):
        form.save()
        return redirect('index')