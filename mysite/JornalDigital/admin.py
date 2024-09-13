from django.contrib import admin
from .models import Edicao, Noticia, Comentario

# Inline para Noticia, permitindo que notícias sejam exibidas dentro de uma Edição
class NoticiaInline(admin.TabularInline):  # ou admin.StackedInline
    model = Noticia
    extra = 1  # Número de formulários de notícias extras para adicionar (opcional)
    fields = ('titulo', 'autor', 'data_publicacao')  # Campos que serão exibidos no inline

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    search_fields = ('titulo',)
    list_filter = ('data',)
    ordering = ('-data',)
    inlines = [NoticiaInline]  # Incluindo as notícias associadas

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'edicao', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('edicao', 'data_publicacao')
    ordering = ('-data_publicacao',)
    raw_id_fields = ('edicao',)
    autocomplete_fields = ('autor',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('noticia', 'autor', 'data_criacao')
    search_fields = ('conteudo',)
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
    raw_id_fields = ('noticia', 'autor')

# Registrando os modelos no admin
admin.site.register(Edicao, EdicaoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
