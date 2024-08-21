from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar-turma'),
    path('<int:id>/', views.visualizar, name='visualizar-turma'),
    path('criar/', views.criar, name='criar-turma'),
    path('editar/<int:turma_id>/', views.editar, name='editar-turma'),
    path('excluir/<int:turma_id>/', views.excluir, name='excluir-turma'),
]