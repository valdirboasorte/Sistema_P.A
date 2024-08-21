from django.shortcuts import render, get_object_or_404, redirect
from agenda.models import Agenda
from .models import PlanoDeEstudo
from .forms import PlanoDeEstudoForm, PlanoDeEstudoAgendaForm
from user.models import Aluno, Orientador
from django.contrib import messages
from turma.models import Turma
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('listar_todos_planos_estudos')
def planoDeEstudoAll(request):
    if request.user.user_type == 'ALU':
        aluno = Aluno.objects.get(user_ptr_id=request.user.id)
        turma = aluno.turma
        planoDeEstudo = PlanoDeEstudo.objects.filter(agenda__turma=turma)
    elif request.user.user_type == 'ORI':
        orientador = Orientador.objects.get(user_ptr_id=request.user.id)
        turmas = Turma.objects.filter(autor=orientador)
        planoDeEstudo = PlanoDeEstudo.objects.filter(agenda__turma__in=turmas)
    
    else:
        planoDeEstudo = PlanoDeEstudo.objects.none() 

    context = {
        'agenda_id' : None,
        'planoDeEstudo': planoDeEstudo,
        'form': PlanoDeEstudoAgendaForm(),
    }
    return render(request, 'planoDeEstudo/list.html', context)

@has_permission_decorator('listar_plano_estudo')
def planoDeEstudo(request, agenda_id):
    planoDeEstudo = PlanoDeEstudo.objects.filter(agenda=agenda_id)

    context = {
        'agenda_id' : agenda_id,
        'planoDeEstudo': planoDeEstudo,
        'form': PlanoDeEstudoForm(),
    }
    return render(request, 'planoDeEstudo/list.html', context)

@has_permission_decorator('visualizar_plano_estudo')
def visualizar(request, planoDeEstudo_id):
    planoDeEstudo = get_object_or_404(PlanoDeEstudo, id=planoDeEstudo_id)
    form = PlanoDeEstudoForm(instance=planoDeEstudo)

    context = {
        'planoDeEstudo': planoDeEstudo,
        'form': form,
    }
    return render(request, 'planoDeEstudo/detalhe.html', context)

@has_permission_decorator('criar_plano_estudo')
def criar(request, agenda_id):
    orientador = Orientador.objects.get(user_ptr_id=request.user.id)
    if request.method == 'POST':
        if agenda_id == 'None':
            form = PlanoDeEstudoAgendaForm(request.POST)
        else:
            agenda = get_object_or_404(Agenda, id=agenda_id)
            form = PlanoDeEstudoForm(request.POST)

        if form.is_valid():
            planoDeEstudo = form.save(commit=False)
            if agenda_id != 'None':
                planoDeEstudo.agenda = agenda
            planoDeEstudo.autor = orientador
            planoDeEstudo.save()
            messages.success(request, "Plano de Estudo Salvo")
            return redirect('visualizar-plano-estudo', planoDeEstudo.id)
        else:
            messages.error(request, "ERRO ao salvar")
            return redirect('listar-agenda')
    
@has_permission_decorator('editar_plano_estudo')    
def editar(request, planoDeEstudo_id):
    if request.method == 'POST':
        planoDeEstudo = get_object_or_404(PlanoDeEstudo, id=planoDeEstudo_id)

        form = PlanoDeEstudoForm(request.POST, instance=planoDeEstudo)
        if form.is_valid():
            form.save()
            messages.success(request, "Plano de estudo editado com sucesso")
            return redirect('visualizar-plano-estudo', planoDeEstudo.id)
        else:
            messages.error(request, "ERRO")
            return redirect('visualizar-plano-estudo', planoDeEstudo.id)

@has_permission_decorator('excluir_plano_estudo')
def excluir(request, planoDeEstudo_id):
    if get_object_or_404(PlanoDeEstudo, id=planoDeEstudo_id):
        planoDeEstudo = get_object_or_404(PlanoDeEstudo, id=planoDeEstudo_id)
        planoDeEstudo.delete()
        messages.success(request, "Plano de estudo excluido com sucesso")
        return redirect('listar-plano-estudo', planoDeEstudo.agenda.id)
    else:
        messages.error(request, "ERRO")
        return redirect('visualizar-plano-estudo', planoDeEstudo.id)