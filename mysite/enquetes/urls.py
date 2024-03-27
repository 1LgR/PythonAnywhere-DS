from . import views
from django.urls import path

app_name = 'enquetes'
urlpatterns = [
    # URL "/enquetes/" --> lista geral das enquetes
    path('', views.index, name= 'index'),
    path('<int:pergunta_id>/', views.detalhes, name = 'detalhes'),
    # URL "/enquetes/55/" --> detalhes da enquete com "id" 55
    path('<int:pergunta_id>/votacao/', views.votacao, name = 'votação'),
    # URL "/enquetes/55/votacao/" --> votacao da enquete 55
    path('<int:pergunta_id>/resultado/', views.resultado, name = 'resultado'),
    # URL "/enquetes/55/resultado/" --> resultado da enquete 55
]