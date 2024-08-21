from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario
from .forms import ComentarioForm
from user.models import Aluno
from planoEstudo.models import PlanoDeEstudo
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('listar_comentario')
def comentarios(request, planoDeEstudo_id):
    comentarios = Comentario.objects.filter(plano_de_estudo=planoDeEstudo_id)

    form = ComentarioForm()

    context = {
        'planoDeEstudo_id' : planoDeEstudo_id,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'comentarios/list.html', context)

@has_permission_decorator('visualizar_comentario')
def visualizar(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    form = ComentarioForm(instance=comentario)

    context = {
        'comentario': comentario,
        'form': form,
    }
    return render(request, 'comentarios/detalhe.html', context)

@has_permission_decorator('criar_comentario')
def criar(request, planoDeEstudo_id):
    aluno = Aluno.objects.get(user_ptr_id=request.user.id)
    plano_de_estudo = get_object_or_404(PlanoDeEstudo, id=planoDeEstudo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.plano_de_estudo = plano_de_estudo
            comentario.autor = aluno
            comentario.save()
            messages.success(request, "Comentário Salvo")
            return redirect('visualizar-comentario', comentario.id)
        else:
            messages.error(request, "ERRO ao salvar")
            return redirect('listar-comentario')

@has_permission_decorator('editar_comentario')   
def editar(request, comentario_id):
    if request.method == 'POST':
        comentario = get_object_or_404(Comentario, id=comentario_id)

        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentário editado com sucesso")
            return redirect('visualizar-comentario', comentario.id)
        else:
            messages.error(request, "ERRO")
            return redirect('visualizar-comentario', comentario.id)

@has_permission_decorator('excluir_comentario')
def excluir(request, comentario_id):
    if get_object_or_404(Comentario, id=comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        comentario.delete()
        messages.success(request, "Plano de estudo excluido com sucesso")
        return redirect('listar-plano-estudo', comentario.plano_de_estudo.id)
    else:
        messages.error(request, "ERRO")
        return redirect('visualizar-comentario', comentario.id)