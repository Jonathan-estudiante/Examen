from django import forms
from .models import *
from .forms import *
from django.contrib.auth.models import User


class TicketsForm(forms.ModelForm):
	
	class Meta:
		model = Tickets
		fields = ('fecha_inicio',
                  'fecha_fin',
                  'descripcion',
                  'estado')
