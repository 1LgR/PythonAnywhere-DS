from django import forms
from .models import Edicao, Noticia, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['data', 'titulo']
        widgets = {
            'data': forms.DateInput(attrs={
                'class': 'datepicker',
                'placeholder': 'Selecione uma data',
                'readonly': 'readonly',
                'type': 'text'
            })
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data > datetime.date.today():
            raise forms.ValidationError("A data deve ser no passado ou no presente.")
        return data

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