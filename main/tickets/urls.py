from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'tickets'

urlpatterns = [
    path('create-tickets', views.createTicket, name='create-tickets'),
    path('list-tickets', views.listTicket, name='list-tickets'),
    path('delete-tickets/<int:id>/', views.deleleTickets, name="delete-tickets"),

]
