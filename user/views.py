from django.shortcuts import render, redirect
from .forms import AlunoCreationForm, OrientadorCreationForm
from django.contrib.auth import login
from django.contrib import messages

def cadastrarAluno(request):
    if request.method == 'POST':
        form = AlunoCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta de aluno criada com sucesso.')
            return redirect('home')
    else:
        form = AlunoCreationForm()
    return render(request, 'registration/signup_form.html', {'form': form, 'tipo': "Aluno"})

def cadastrarOrientador(request):
    if request.method == 'POST':
        form = OrientadorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta de orientador criada com sucesso.')
            return redirect('home')
    else:
        form = OrientadorCreationForm()
    return render(request, 'registration/signup_form.html', {'form': form, 'tipo': "Orientador"})
