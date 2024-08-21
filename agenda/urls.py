
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.agenda, name='listar-agenda'),
    path('<int:agenda_id>/', views.visualizar, name='visualizar-agenda'),
    path('criar/', views.criar, name='criar-agenda'),
    path('editar/<int:agenda_id>/', views.editar, name='editar-agenda'),
    path('excluir/<int:agenda_id>/', views.excluir, name='excluir-agenda'),
]