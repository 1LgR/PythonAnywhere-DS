from django.shortcuts import render
from django.views import View
from .models import Edicao

class IndexView(View):
    def get(self, request, *args, **kwargs):
        ultima_edicao = Edicao.objects.order_by('-data').first()
        return render(request, 'JornalDigital/index.html', {'edicao': ultima_edicao})