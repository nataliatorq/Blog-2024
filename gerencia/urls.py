from django.urls import path

from . import views
from .views import cadastrar_noticia, editar_noticia, inicio_gerencia, listagem_noticia

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    # Add your URL patterns here
    path("categorias/", views.categoria_listar, name="categoria_listar"),
    path("categorias/cadastrar/", views.categoria_criar, name="categoria_cadastrar"),
    path("categorias/editar/<int:id>", views.categoria_editar, name="categoria_editar"),
    path("categorias/remover/<int:id>", views.categoria_remover, name="categoria_remover"),
]