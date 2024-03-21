from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Habitacion, Reserva
from .forms import ReservaForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticar al usuario
            user = form.get_user()
            auth_login(request, user)
            # Redirigir al usuario a la página de inicio
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'reservas/habitaciones.html', {'habitaciones': habitaciones})

def reservas(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'reservas/reservas.html', {'habitaciones': habitaciones})

def index(request):
    return render(request, 'reservas/index.html')

@login_required
def reservar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.habitacion = habitacion
            reserva.save()

            # Marcar la habitación como no disponible
            habitacion.disponible = False
            habitacion.save()

            return redirect('mis_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/reservar_habitacion.html', {'form': form, 'habitacion': habitacion})

@login_required
def mis_reservas(request):
    # reservas asociadas con el usuario actual
    reservas_usuario = Reserva.objects.filter(usuario=request.user)

    # Imprimir las reservas obtenidas
    print("Reservas del usuario:", reservas_usuario)
    
    for reserva in reservas_usuario:
        print("Reserva:", reserva)

    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas_usuario})

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    habitacion = reserva.habitacion

    if request.user == reserva.usuario:
        reserva.delete()
        
        # Marcar la habitación como disponible nuevamente
        habitacion.disponible = True
        habitacion.save()

    return redirect('mis_reservas')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
