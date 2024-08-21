
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.planoDeEstudoAll, name='listar-todos-planos-estudos'),
    path('<int:agenda_id>/', views.planoDeEstudo, name='listar-plano-estudo'),
    path('detalhe/<int:planoDeEstudo_id>/', views.visualizar, name='visualizar-plano-estudo'),
    path('criar/<str:agenda_id>/', views.criar, name='criar-plano-estudo'),
    path('editar/<int:planoDeEstudo_id>/', views.editar, name='editar-plano-estudo'),
    path('excluir/<int:planoDeEstudo_id>/', views.excluir, name='excluir-plano-estudo'),
]