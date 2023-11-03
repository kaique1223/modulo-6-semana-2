from django.shortcuts import render
from django.http import HttpResponse
from base.forms import contatoform,reservaform

def inicio(request):
    
    return render(request,'inicio.html')

def contato(request):
    sucesso = False

    if request.method == 'GET':
        form = contatoform()
    else:
        form = contatoform(request.POST)
        if form.is_valid():
            sucesso = True
         
            

    contexto = {
        'telefone' : '(99)99999.9999',
        'responsavel' : 'MARIA ',
        'form': form,
        'sucesso': sucesso
        
        }
   
    return render(request,'contato.html',contexto)
def reserva(request):
    sucesso2 = False
    if request.method == 'GET':
        form2 = reservaform()
    else:
        form2 = reservaform(request.POST)
        if form2.is_valid():
            sucesso2 = True

            
    contexto2 = {
            'sucesso2': sucesso2,
            'form2': form2
        }
   
    return render(request,'reserva.html',contexto2)