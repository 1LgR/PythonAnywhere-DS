from django.shortcuts import get_object_or_404, render
from django.views import View
from .forms import ComentarioForm
from .models import Noticia



class ExibirNoticiaView(View):
    def get(self, request, noticia_id, *args, **kwargs):
        noticia = get_object_or_404(Noticia, id=noticia_id)
        comentarios = noticia.comentarios.all()
        form = ComentarioForm()
        return render(request, 'JornalDigital/exibir_noticia.html', {
            'noticia': noticia,
            'comentarios': comentarios,
            'form': form
        })