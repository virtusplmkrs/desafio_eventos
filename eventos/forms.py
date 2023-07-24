":*******************************************************************************************:"
" Application: Agenda de Eventos                                               Eventos (\/¬) :"
" Date       : __/__/____                                           Versão: DjPy: 01.00.00-X :"
" Dev        :                                                                               :"
" Description:                                                                               :"
":*******************************************************************************************:"
" Application: Agenda de Eventos                                               Eventos (\/¬) :"
" Date       : 21/07/2023                                           Versão: DjPy: 01.00.00-X :"
" Dev        : Alexandre Yuri                                                                :"
" Description: Create version Master                                                         :"
":*******************************************************************************************:"


from django import forms 
from django.forms import ModelForm
from .models import Local, Evento


class LocalForm(ModelForm):
    class Meta:
        model = Local
        # se quizer todos os campos
        #fields = "__all__"
        # se quizer campos especificos
        fields = ('nome', 'endereco', 'cep', 'fone', 'web', 'email')
        labels = {
            'nome': 'Local',
            'endereco': 'Endereço',
            'cep': 'CEP',
            'fone': 'Telefone',
            'web': 'HomPage',
            'email': 'Email',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do local'}),
            'endereco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço do local'}),
            'cep': forms.TextInput(attrs={'class':'form-control', 'placeholder':'cep do local'}),
            'fone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'telefone do local'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'pagina do evento'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email para contato'}),
        }

# Administrador
class EventoFormAdmin(ModelForm):
    class Meta:
        model = Evento
        # se quizer todos os campos
        #fields = "__all__"
        # se quizer campos especificos
        fields = ('nome', 'data_evento', 'data_final', 'local', 'promoter', 'participantes', 'descricao')
        labels = {
            'nome': '',
            'data_evento': 'YYYY-MM-DD HH:MM:SS',
            'data_final': 'YYYY-MM-DD HH:MM:SS',
            'local': 'local',
            'promoter': 'promoter',
            'participantes': 'participantes',
            'descricao': '',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do evento'}),
            'data_evento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'data do evento'}),
            'data_final': forms.TextInput(attrs={'class':'form-control', 'placeholder':'data final'}),
            'local': forms.Select(attrs={'class':'form-select', 'placeholder':'Local do evento'}),
            'promoter': forms.Select(attrs={'class':'form-select', 'placeholder':'Promoter do evento'}),
            'participantes': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Participantes do evento'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição do evento'}),
        }

## Usuarios
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        # se quizer todos os campos
        #fields = "__all__"
        # se quizer campos especificos
        fields = ('nome', 'data_evento', 'data_final', 'local', 'participantes', 'descricao')
        labels = {
            'nome': '',
            'data_evento': 'YYYY-MM-DD HH:MM:SS',
            'data_final': 'YYYY-MM-DD HH:MM:SS',
            'local': 'local',
            'participantes': 'participantes',
            'descricao': '',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do evento'}),
            'data_evento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'data do evento'}),
            'data_final': forms.TextInput(attrs={'class':'form-control', 'placeholder':'data final'}),
            'local': forms.Select(attrs={'class':'form-select', 'placeholder':'Local do evento'}),
            'participantes': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Participantes do evento'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição do evento'}),
        }
