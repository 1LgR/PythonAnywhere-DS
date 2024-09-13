from django import forms
from .models import Edicao, Noticia, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['data', 'titulo']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['edicao', 'titulo', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']