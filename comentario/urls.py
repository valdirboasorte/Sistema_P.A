
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [    
    path('<int:planoDeEstudo_id>/', views.comentarios, name='listar-comentario'),
    path('visualizar/<int:comentario_id>/', views.visualizar, name='visualizar-comentario'),
    path('criar/<int:planoDeEstudo_id>/', views.criar, name='criar-comentario'),
    path('editar/<int:comentario_id>/', views.editar, name='editar-comentario'),
    path('excluir/<int:comentario_id>/', views.excluir, name='excluir-comentario'),
]