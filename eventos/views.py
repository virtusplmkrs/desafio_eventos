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


from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Evento, Local
from .forms import LocalForm, EventoForm, EventoFormAdmin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def evento_local(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'eventos/evento_local.html',{
            'evento':evento,})

def local_evento(request, local_id):
    local = Local.objects.get(id=local_id)
    eventos = local.evento_set.all()
    if local:
        return render(request, 'eventos/local_evento.html',{
            'eventos':eventos,})
    else:
        messages.success(request, "Não exite eventos para esse local!")
        return redirect('admin-aprova')

def admin_aprova(request):
    list_local = Local.objects.all()
    evento_count = Evento.objects.all().count()
    local_count = Local.objects.all().count()
    evento_list = Evento.objects.all().order_by('-data_evento')
    if request.user.is_superuser:
        if request.method=='POST':
            id_list = request.POST.getlist("boxes")
            #print(id_list)
            evento_list.update(aprovado=False)
            for x in id_list:
                Evento.objects.filter(pk=int(x)).update(aprovado=True)
            messages.success(request, "Confira a lista de eventos aprovados!")
            return redirect('list-evento')
        else:
            return render(request, 'eventos/admin_aprova.html',
                  {'evento_list':evento_list,
                   'evento_count':evento_count,
                   'local_count':local_count,
                   'list_local':list_local,
                   })
    else:
        messages.success(request, "Você precisa estar logado para ter acesso a esse recurso")
        return redirect('home')
    
def busca_eventos(request):
    if request.method == "POST":
        searched = request.POST['searched']
        evento = Evento.objects.filter(descricao__contains=searched)
        return render(request, 'eventos/busca_evento.html',
                    {'searched':searched, 'evento':evento})
    else:
        return render(request, 'eventos/busca_evento.html',
                  {})
    
def meus_eventos(request):
    if request.user.is_authenticated:
        user_log = request.user.id
        eventos = Evento.objects.filter(promoter=user_log)
        return render(request, 'eventos/my_eventos.html', {"eventos":eventos})
    else:
        messages.success(request, ("Você não tem Permissão para visualizar essa pagina."))
        return redirect('home')

def delete_local(request, local_id):
    local = Local.objects.get(pk=local_id)
    local.delete()
    form = LocalForm(request.POST or None, instance=local)
    return redirect('list-local')
    
def delete_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    if request.user == evento.promoter:
        evento.delete()
        #form = EventoForm(request.POST or None, instance=evento)
        messages.success(request, ("Evento Excluido!!"))
        return redirect('list-evento')
    else:
        #form = EventoForm(request.POST or None, instance=evento)
        messages.success(request, ("Você não tem Permissão de exclussão!!"))
        return redirect('list-evento')
    
def list_eventos(request):
    evento_list = Evento.objects.all()
    return render(request, 'eventos/evento_list.html',
                  {'evento_list':evento_list})

def update_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    if request.user.is_superuser:
        form = EventoFormAdmin(request.POST or None, instance=evento)
    else:
        form = EventoForm(request.POST or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('list-evento')
    
    return render(request, 'eventos/update_evento.html',
                  {'evento': evento, 'form':form})

def add_evento(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventoFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_evento?submitted=True')
            
        else:
            form = EventoForm(request.POST)
            if form.is_valid():
                #form.save()
                evento = form.save(commit=False)
                evento.promoter = request.user
                evento.save()
                return HttpResponseRedirect('/add_evento?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventoFormAdmin
        else:
            form = EventoForm

        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'eventos/add_evento.html', {'form':form, 'submitted':submitted})

def update_local(request, local_id):
    local = Local.objects.get(pk=local_id)
    form = LocalForm(request.POST or None, instance=local)
    if form.is_valid():
        form.save()
        return redirect('list-local')
    
    return render(request, 'eventos/update_local.html',
                  {'local': local, 'form':form})

def busca_local(request):
    if request.method == "POST":
        searched = request.POST['searched']
        local = Local.objects.filter(nome__contains=searched)
        return render(request, 'eventos/busca_local.html',
                    {'searched':searched, 'local':local})
    else:
        return render(request, 'eventos/busca_local.html',
                  {})
    
def ficha_local(request, local_id):
    local = Local.objects.get(pk=local_id)
    #local_prop = User.objects.get(pk=local.promoter)
    return render(request, 'eventos/ficha_local.html',
                  {'local': local,})

def list_local(request):
    #list_local = Local.objects.all().order_by('nome')
    list_local = Local.objects.all()

    p = Paginator(Local.objects.all(), 3)
    page = request.GET.get('page')
    local = p.get_page(page)
    
    nums = "a" * local.paginator.num_pages

    return render(request, 'eventos/local.html',
                  {'local_list':list_local, 'local':local, 'nums':nums})

def add_local(request):
    submitted = False
    if request.method == "POST":
       form = LocalForm(request.POST)
       if form.is_valid():
           local = form.save(commit=False)
           local.promoter = request.user.id
           local.save()
           #form.save()
           return HttpResponseRedirect('/add_local?submitted=True')
    else:
        form = LocalForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'eventos/add_local.html', {'form':form, 'submitted':submitted})

def all_eventos(request):
    evento_list = Evento.objects.all().order_by('data_evento')
    return render(request, 'eventos/evento_list.html',
                  {'evento_list':evento_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    nome = 'Yuri'
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    
    
    evento_list = Evento.objects.filter(
        data_evento__year=year,
        data_evento__month=month_number
    )
    
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M - %p')

    return render(request, 
                  'eventos/home.html', {
                      'Nome':nome,
                      'year':year,
                      'month':month,
                      'month_number':month_number,
                      "cal":cal,
                      "current_year":current_year,
                      "time":time,
                      "evento_list":evento_list,
                  })