from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edicao, Noticia, Comentario
from .forms import EdicaoForm, NoticiaForm, ComentarioForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages




class IndexView(View):
    def get(self, request, *args, **kwargs):
        ultima_edicao = Edicao.objects.order_by('-data').first()
        return render(request, 'JornalDigital/index.html', {'edicao': ultima_edicao})

def Cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Você já pode fazer login.')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'JornalDigital/cadastro.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('JonalDigital/index.html')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    form = AuthenticationForm()
    return render(request, 'JornalDigital/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('index')

class ListarEdicoesView(ListView):
    model = Edicao
    template_name = 'JornalDigital/listar_edicoes.html'
    context_object_name = 'edicoes'
    ordering = ['-data']

class ExibirEdicaoView(DetailView):
    model = Edicao
    template_name = 'JornalDigital/exibir_edicao.html'
    context_object_name = 'edicao'
    pk_url_kwarg = 'edicao_id'

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


class CadastrarEdicaoView(LoginRequiredMixin, CreateView):
    model = Edicao
    form_class = EdicaoForm
    template_name = 'JornalDigital/cadastrar_edicao.html'

    def form_valid(self, form):
        form.save()
        return redirect('index')


class CadastrarNoticiaView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'JornalDigital/cadastrar_noticia.html'

    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.autor = self.request.user
        noticia.save()
        return redirect('exibir_edicao', edicao_id=noticia.edicao.id)

class PesquisarView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            noticias = Noticia.objects.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))
        else:
            noticias = Noticia.objects.none()
        return render(request, 'JornalDigital/pesquisar.html', {'noticias': noticias, 'query': query})