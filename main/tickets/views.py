from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import*
# Create your views here.
class CreateTicket(CreateView):
    model = Tickets
    form_class = TicketsForm
    template_name = 'tickets/create-tickets.html'
    success_url = reverse_lazy('usuarios:homepage')


def createTicket(request):
    form_registro = TicketsForm(prefix="registro_form")

    context = { 
            'form_registro' : form_registro, 
            }
    if request.method == "POST":      
        form_registro = TicketsForm(request.POST, prefix="registro_form")
        if form_registro.is_valid():
            tickets = form_registro.save(commit=False)
            tickets.usuario = request.user
            tickets.save()
            return render(request, 'inicio/inicio.html', context)
            

    return render(request, 'tickets/create-tickets.html',  context)

def listTicket(request):
    lista_tickets = Tickets.objects.all()
    contexto = {
        'lista_tickets': lista_tickets
    }
    return render(request, 'tickets/list-tickets.html', contexto)

def deleleTickets(request, id):
    tickets = Tickets.objects.get(id=id)
    tickets.delete()
    return redirect("tickets:list-tickets")