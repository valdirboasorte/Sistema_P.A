from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    dia = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
    )
    class Meta:
        model = Agenda
        fields = ['dia', 'descricao', 'local']

class AgendaOrientadorForm(forms.ModelForm):
    dia = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}), 
    )
    class Meta:
        model = Agenda
        fields = ['dia', 'descricao', 'local', 'status']