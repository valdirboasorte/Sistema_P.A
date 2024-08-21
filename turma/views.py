from django.shortcuts import redirect, render, get_object_or_404
from .models import Turma
from .forms import TurmaForm
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('listar_turma')
def listar(request):
    if request.method == 'GET':  
        if request.user.user_type == 'ORI':
            turmas = Turma.objects.filter(autor=request.user)
        else:
            turmas = Turma.objects.filter(aluno=request.user)

        formTurma = TurmaForm()

        context = {
            'turmas': turmas,
            'formTurma': formTurma,
        }

        return render(request, 'turma/list.html',context)

@has_permission_decorator('visualizar_turma')
def visualizar(request, id):
    turma = get_object_or_404(Turma, id=id)
    formTurma = TurmaForm(instance=turma)

    context = {
        'turma': turma,
        'formTurma': formTurma,
    }
    return render(request, 'turma/detalhe.html', context)


@has_permission_decorator('criar_turma')
def criar(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.autor = request.user.orientador
            turma.save()
            messages.success(request, "Turma criada com sucesso")
            return redirect('listar-turma')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-turma')


@has_permission_decorator('editar_turma')
def editar(request, turma_id):
    if request.method == 'POST':
        turma = Turma.objects.get(pk=turma_id)
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, "Turma editada com sucesso")
            return redirect('listar-turma')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-turma')

@has_permission_decorator('excluir_turma')
def excluir(request, turma_id):
    if get_object_or_404(Turma, pk=turma_id):
        turma = get_object_or_404(Turma, pk=turma_id)
        turma.delete()
        messages.success(request, "Turma excluida com sucesso")
        return redirect('listar-turma')
    else:
        messages.error(request, "ERRO")
        return redirect('listar-turma')