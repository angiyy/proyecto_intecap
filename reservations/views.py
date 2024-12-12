from django.shortcuts import render, get_object_or_404, redirect
from .models import Habitacion, Cliente, Reserva
from .forms import HabitacionForm, ClienteForm,ReservaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect




def index(request):
    return render(request, 'index.html')
def login_view(request):
    return render(request, 'login.html')

# Vista para el panel principal
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('logout_success')

# Vista para la página de cierre de sesión exitoso
def logout_success(request):
    return render(request, 'logout_success.html')

@login_required
def admin_dashboard(request):
    return render(request, 'reservas/admin_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('logout_success')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Inicia la sesión
            if user.is_superuser:  # Si es superusuario
                return redirect('admin_dashboard')  # Redirige al panel de administración
            else:
                return redirect('habitaciones')  # Redirige a otra vista si no es superusuario
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'login.html')

# Mostrar todas las habitaciones
def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'lista.html', {'habitaciones': habitaciones})

# Crear una nueva habitación
def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'habitaciones/formulario.html', {'form': form})

# Editar una habitación existente
def editar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('lista_habitaciones')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'habitaciones/formulario.html', {'form': form})

# Eliminar una habitación
def eliminar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('lista_habitaciones')
    return render(request, 'habitaciones/eliminar.html', {'habitacion': habitacion})


# Listar Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

# Crear Cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/formulario.html', {'form': form})

# Editar Cliente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/formulario.html', {'form': form})

# Eliminar Cliente
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})

# Listar Reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista.html', {'reservas': reservas})

# Crear Reserva
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/formulario.html', {'form': form})

# Editar Reserva
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/formulario.html', {'form': form})

# Eliminar Reserva
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/eliminar.html', {'reserva': reserva})

