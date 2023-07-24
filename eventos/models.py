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


from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
#from dateutil.relativedelta import relativedelta



class Local(models.Model):
    nome = models.CharField('Nome Local', max_length=120)
    endereco = models.CharField(max_length=300)
    cep = models.CharField('Cep', max_length=8)
    fone = models.CharField('Telefone Contato', max_length=11, blank=True)
    web = models.URLField('HomePage', blank=True)
    email= models.EmailField('Email Contato', blank=True)

    def __str__(self):
        return self.nome

class MyEventoUser(models.Model):
    nome = models.CharField(max_length=30)
    fuso = models.CharField(max_length=6, default="1")
    email = models.EmailField('Email Promoter')
    def __str__(self):
        return self.nome + ' ' + self.fuso + ' horas'

class Evento(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    data_evento = models.DateTimeField(verbose_name='Data Evento')
    data_final = models.DateTimeField(verbose_name='Data Final')
    local = models.ForeignKey(Local, blank=True, null=True, on_delete=models.CASCADE)
    promoter = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Gerente')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    participantes = models.ManyToManyField(MyEventoUser, blank=True)
    aprovado = models.BooleanField('Aprovado', default=False)

    def __str__(self):
        return self.nome
    
    @property
    def Days_till(self):
        today = date.today()
        days_till = self.data_evento.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped
    
    @property
    def Is_Past(self):
        today = date.today()
        if self.data_evento.date() > today:
            thing = "Vai acontecer em "
        elif self.data_evento.date() < today:
            thing = "Já Aconteceu em "
        else:
            thing = ""
        return thing
    
    @property
    def Days_dif(self):
        days_dif = abs((self.data_final.date() - self.data_evento.date()).days)
        days_dif_stripped = str(days_dif).split(",", 1)[0]
        days_dif_stripped = int(days_dif_stripped) + 1
        return days_dif_stripped
    
