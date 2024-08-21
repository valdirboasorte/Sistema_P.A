from django import forms
from .models import PlanoDeEstudo

class PlanoDeEstudoForm(forms.ModelForm):
    class Meta:
        model = PlanoDeEstudo
        fields = ['descricao']

class PlanoDeEstudoAgendaForm(forms.ModelForm):
    class Meta:
        model = PlanoDeEstudo
        fields = ['descricao', 'agenda']