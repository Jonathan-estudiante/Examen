from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import*
from .forms import*
# Create your views here.
def homepage(request):
    return render(request, "inicio/inicio.html")

# Función para crear un usuario
def registroUsuario(request):

    if request.method == "POST":
        form_registro = UserCreationForm(request.POST)
        if form_registro.is_valid():
            usuario = form_registro.save()
            nombre_usuario = form_registro.cleaned_data.get('username')
            messages.success(
                request, f"Nueva Cuenta Creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido logeado como {nombre_usuario}")
            return redirect("usuarios:homepage")
        else:
            for msg in form_registro.error_messages:
                messages.error(request, f"{msg}: {form_registro.error_messages[msg]}")

    form_registro = UserCreationForm
    return render(request, "usuarios/login.html", {"form_registro": form_registro})
# Función para salir de la página
def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente") 
    return redirect("usuarios:homepage")
# Función para entrar si ya estamos registrado
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estás logeado como {usuario}")
                return redirect("usuarios:homepage")
            else:
                messages.error(request, "Usuario o contraseña equivocada")
        else:
            messages.error(request, "Usuario o contraseña equivocada")
    form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})
# Clase para crear un curso