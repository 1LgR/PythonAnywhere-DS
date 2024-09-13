from django.db import models
from django.contrib.auth.models import User

class Edicao(models.Model):
    data = models.DateField()
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.data}"
        
class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, related_name='noticias')
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='noticias')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.noticia.titulo}"