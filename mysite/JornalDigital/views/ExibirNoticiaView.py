from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Noticia, Comentario
from .forms import ComentarioForm





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

    def post(self, request, noticia_id, *args, **kwargs):
        noticia = get_object_or_404(Noticia, id=noticia_id)

        if 'delete_comentario_id' in request.POST:
            comentario = get_object_or_404(Comentario, id=request.POST['delete_comentario_id'])
            if comentario.autor == request.user or request.user.is_staff:
                comentario.delete()
            return redirect('exibir_noticia', noticia_id=noticia.id)

        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.autor = request.user
            comentario.save()
            return redirect('exibir_noticia', noticia_id=noticia.id)

        comentarios = noticia.comentarios.all()
        return render(request, 'JornalDigital/exibir_noticia.html', {
            'noticia': noticia,
            'comentarios': comentarios,
            'form': form
        })