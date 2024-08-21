# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno, Orientador
from rolepermissions.roles import assign_role

class AlunoCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Aluno
        fields = UserCreationForm.Meta.fields + ('nome', 'cpf', 'user_type', 'matricula', 'turma')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].initial = 'ALU'
        self.fields['user_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        assign_role(user, 'aluno')
        if commit:
            user.save()
        return user
    
class OrientadorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Orientador
        fields = UserCreationForm.Meta.fields + ('nome', 'cpf', 'user_type', 'contato')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].initial = 'ORI'
        self.fields['user_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        assign_role(user, 'orientador')
        if commit:
            user.save()
        return user