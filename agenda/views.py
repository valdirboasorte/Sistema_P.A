from django.shortcuts import render, get_object_or_404, redirect
from turma.models import Turma
from .models import Agenda
from .forms import AgendaForm, AgendaOrientadorForm
from user.models import Aluno, Orientador
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('listar_agenda')
def agenda(request):
    if request.user.user_type == 'ALU':
        aluno = Aluno.objects.get(user_ptr_id=request.user.id)
        turma = aluno.turma
        agendamentos = Agenda.objects.filter(turma=turma)
    elif request.user.user_type == 'ORI':
        orientador = Orientador.objects.get(user_ptr_id=request.user.id)
        turmas_criadas = Turma.objects.filter(autor=orientador)
        agendamentos = Agenda.objects.filter(turma__in=turmas_criadas)

    form = AgendaForm()

    context = {
        'agendamentos': agendamentos,
        'form': form,
    }
    return render(request, 'agenda/list.html', context)

@has_permission_decorator('visualizar_agenda')
def visualizar(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)
    form = AgendaOrientadorForm(instance=agenda)

    context = {
        'agenda': agenda,
        'form': form,
    }
    return render(request, 'agenda/detalhe.html', context)

@has_permission_decorator('criar_agenda')
def criar(request):
    aluno = Aluno.objects.get(user_ptr_id=request.user.id)
    turma = aluno.turma

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit=False)
            agenda.turma = turma
            agenda.autor = aluno
            agenda.save()
            messages.success(request, "Agendamento Salvo")
            return redirect('visualizar-agenda', agenda.id)
        else:
            messages.error(request, "ERRO ao salvar")
            return redirect('listar-agenda')

@has_permission_decorator('editar_agenda')  
def editar(request, agenda_id):
    if request.method == 'POST':
        agenda = get_object_or_404(Agenda, id=agenda_id)

        form = AgendaOrientadorForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            messages.success(request, "Agendamento editado com sucesso")
            return redirect('visualizar-agenda', agenda.id)
        else:
            messages.error(request, "ERRO")
            return redirect('visualizar-agenda', agenda.id)

@has_permission_decorator('excluir_agenda')
def excluir(request, agenda_id):
    if get_object_or_404(Agenda, id=agenda_id):
        agenda = get_object_or_404(Agenda, id=agenda_id)
        agenda.delete()
        messages.success(request, "Agendamento excluido com sucesso")
        return redirect('listar-agenda')
    else:
        messages.error(request, "ERRO")
        return redirect('visualizar-agenda', agenda_id)