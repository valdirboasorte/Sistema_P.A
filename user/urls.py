
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [    
    path('signup/aluno/', views.cadastrarAluno, name='cadastrar-aluno'),
    path('signup/orientador/', views.cadastrarOrientador, name='cadastrar-orientador'),
]